# Multi-stage build for Python MCP server with scientific computing libraries
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install Python dependencies
COPY mcp-server/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Final stage - runtime image
FROM python:3.11-slim

# Install runtime dependencies only
RUN apt-get update && apt-get install -y \
    libopenblas0 \
    liblapack3 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy application code
COPY mcp-server/ ./mcp-server/
COPY scripts/ ./scripts/
COPY knowledge-bases/ ./knowledge-bases/

# Set Python path to include necessary directories
ENV PYTHONPATH="/app:/app/scripts:/app/mcp-server"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:3000/health', timeout=5)" || exit 1

# Command to run the application
CMD ["python", "mcp-server/mcp_pinecone_server.py", "--cloud", "--port", "3000"]