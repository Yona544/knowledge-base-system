# Fly.io Deployment Guide for Advantage MCP Server

## Overview

The Advantage MCP Server is now deployed on Fly.io, providing a robust, scalable platform for the Pinecone knowledge base system.

## Deployment Details

- **App Name**: `advantage-mcp-server`
- **URL**: https://advantage-mcp-server.fly.dev
- **Region**: `ewr` (Newark - NY region)
- **Runtime**: Python 3.11 with scientific computing libraries
- **Port**: 3000 (HTTP/SSE)
- **Authentication**: Bearer token required

## Application Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   MCP Client    │───▶│  Fly.io App      │───▶│  Pinecone DB    │
│   (Local)       │    │  Port 3000       │    │  (Vector Store) │
└─────────────────┘    │  Bearer Auth     │    └─────────────────┘
                       │  advantage-mcp   │           │
                       │  -server         │           ▼
                       └──────────────────┘    ┌─────────────────┐
                                               │   OpenAI API    │
                                               │  (Embeddings)   │
                                               └─────────────────┘
```

## Environment Variables (Configured as Fly.io Secrets)

- `OPENAI_API_KEY`: OpenAI API key for embeddings and LLM
- `PINECONE_API_KEY`: Pinecone API key for vector database
- `PINECONE_HOST`: Pinecone serverless host URL
- `PINECONE_INDEX`: Vector index name (advantage-v2)
- `PINECONE_ENVIRONMENT`: Pinecone environment (us-east-1)
- `MCP_API_KEY`: Bearer token for API authentication (dev-local-123)

## Available MCP Tools

1. **search_kb**: Hybrid search in knowledge base
2. **get_doc**: Fetch specific markdown documents
3. **synthesize_answer**: Generate answers with optional citations
4. **list_knowledge_bases**: List available repositories
5. **get_repository_stats**: Get usage statistics
6. **list_recent_updates**: View recent activity
7. **health_check**: Check system connectivity

## Usage with MCP Client

Connect to the server using:
- **URL**: `https://advantage-mcp-server.fly.dev`
- **Authentication**: Bearer token: `dev-local-123`

Example MCP configuration:
```json
{
  "mcpServers": {
    "pinecone-kb-sse": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sse"],
      "env": {
        "MCP_SERVER_URL": "https://advantage-mcp-server.fly.dev",
        "MCP_SERVER_API_KEY": "dev-local-123"
      }
    }
  }
}
```

## Deployment Commands

### Initial Setup (Already Completed)
```bash
# Install Fly.io CLI
iex (iwr https://fly.io/install.ps1 -useb)

# Authenticate
flyctl auth login

# Create app
flyctl apps create advantage-mcp-server --org personal

# Set secrets
flyctl secrets set OPENAI_API_KEY="your-key" --app advantage-mcp-server
flyctl secrets set PINECONE_API_KEY="your-key" --app advantage-mcp-server
flyctl secrets set PINECONE_HOST="your-host" --app advantage-mcp-server
flyctl secrets set PINECONE_INDEX="advantage-v2" --app advantage-mcp-server
flyctl secrets set PINECONE_ENVIRONMENT="us-east-1" --app advantage-mcp-server
flyctl secrets set MCP_API_KEY="dev-local-123" --app advantage-mcp-server
```

### Deploy Updates
```bash
flyctl deploy --app advantage-mcp-server
```

### Monitor Application
```bash
# View logs
flyctl logs --app advantage-mcp-server

# Check status
flyctl status --app advantage-mcp-server

# Scale if needed
flyctl scale count 2 --app advantage-mcp-server
```

## Key Features

✅ **Multi-stage Docker build** - Optimized for scientific computing dependencies  
✅ **Bearer token authentication** - Secure API access  
✅ **Auto-scaling** - Stops when idle, starts on demand  
✅ **Persistent storage** - 1GB volume for data  
✅ **Health monitoring** - Application health checks  
✅ **SSL/TLS** - HTTPS enforced  

## Performance

- **Build Time**: ~3-4 minutes (due to scientific libraries)
- **Start Time**: ~7 seconds from cold start
- **Memory**: 1GB allocated
- **CPU**: 1 shared vCPU

## Migration Benefits vs Replit

- ✅ Better performance and reliability
- ✅ Custom domain capability
- ✅ Professional deployment tooling
- ✅ Better scaling options
- ✅ CLI-based workflow
- ✅ Integrated monitoring
- ✅ Cost-effective auto-sleep

## Troubleshooting

### Common Issues

1. **503 Service Unavailable**: Machine may be starting up (wait ~10 seconds)
2. **401 Unauthorized**: Check Bearer token in Authorization header
3. **Import Errors**: Ensure Dockerfile includes all required dependencies

### Debug Commands
```bash
# SSH into machine
flyctl ssh console --app advantage-mcp-server

# View real-time logs
flyctl logs --app advantage-mcp-server -f

# Restart application
flyctl machines restart --app advantage-mcp-server
```

## Cost Optimization

The app uses Fly.io's auto-stop feature:
- Stops when idle (no requests)
- Starts automatically on first request
- Only pay for active usage time
- Persistent storage maintained during stops