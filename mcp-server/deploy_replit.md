# Deploying Pinecone KB MCP Server on Replit

This guide explains how to run the Python MCP server on Replit over HTTP SSE with Bearer authentication.

- Server entry: [mcp-server/mcp_pinecone_server.py](mcp-server/mcp_pinecone_server.py)
- Config: [mcp-server/mcp_config.py](mcp-server/mcp_config.py)
- Pinecone helpers: [mcp-server/pinecone_client.py](mcp-server/pinecone_client.py)
- Requirements: [mcp-server/requirements.txt](mcp-server/requirements.txt)

## What you get

- HTTP SSE endpoint (default path: `/sse`) served on port 3000 with Authorization: Bearer
- Tools: search and synthesis over Pinecone hybrid retrieval plus repository utilities and health checks
- Per-call overrides for index, repository (namespace), models, and OpenAI base URL
- **Automatic dependency installation** via `install.sh` and `replit.nix`

## Prerequisites

- Replit account
- Pinecone Serverless index available in your region (default: us-west1-gcp-free)
- Knowledge base contents synced to the repo under `knowledge-bases/`
- Valid API keys:
  - OPENAI_API_KEY
  - PINECONE_API_KEY

## Create the Repl

1) In Replit, create a new "Python" Repl.
2) Connect this GitHub repo (recommended) or copy the following folders/files:
   - `mcp-server/` (entire directory)
   - `knowledge-bases/` (at least the repos/namespaces you intend to query)
   - `.replit` (Replit configuration)
   - `replit.nix` (system dependencies)
   - `install.sh` (dependency installation script)

## Set Secrets (Environment Variables)

In Replit, open the "Secrets" pane and add:

- OPENAI_API_KEY = your OpenAI API key
- PINECONE_API_KEY = your Pinecone API key
- MCP_API_KEY = a shared secret for Bearer auth (client must send this as Authorization: Bearer)
- PINECONE_INDEX = knowledge-base-index
- PINECONE_ENVIRONMENT = us-west1-gcp-free

Optional (global defaults; all can be overridden per call):
- EMBED_MODEL = text-embedding-3-small
- LLM_MODEL = gpt-4o-mini
- OPENAI_BASE_URL = custom OpenAI-compatible endpoint
- MCP_SERVER_PORT = 3000

## Automatic Installation & Startup

The project is configured for automatic setup:

- **`replit.nix`**: Installs system dependencies (Python 3.11, scikit-learn dependencies, etc.)
- **`install.sh`**: Installs Python packages from `requirements.txt`
- **`.replit`**: Configures Replit to run the installation script first, then start the server

Simply click "Run" in Replit - dependencies will install automatically and the server will start.

## Manual Installation (if needed)

If automatic installation fails, run in the Replit shell:
```bash
pip install -r mcp-server/requirements.txt
python mcp-server/mcp_pinecone_server.py --cloud --port 3000
```

Replit will expose a public URL (e.g., `https://your-repl-name.your-user.repl.co`). The SSE endpoint will be:

- `https://your-repl-domain/sse`

## Client configuration example (Windsurf MCP)

Add/update your MCP settings (example schema):

```
{
  "mcpServers": {
    "pinecone-kb-sse": {
      "type": "sse",
      "url": "https://your-repl-domain/sse",
      "headers": {
        "Authorization": "Bearer ${env:MCP_API_KEY}"
      }
    }
  }
}
```

Notes:
- Use the exact Replit public URL for the `url`.
- Ensure your local environment has the same MCP_API_KEY value as the one in Replit or replace `${env:MCP_API_KEY}` with the literal secret.

## Tools available

Server registers these tools:

- list_knowledge_bases
- get_repository_stats
- list_recent_updates
- search_kb
- get_doc
- synthesize_answer
- answer_knowledge

Default top-k is 8 (k=8) for search/synthesis.

Per-call overrides supported (no redeploy required):
- indexOverride: target a different Pinecone index
- repository: the Pinecone namespace to query
- embedModel: embedding model override
- llmModel: chat model override
- openaiBaseUrl: OpenAI-compatible base URL override

## Basic validation

- Confirm the Replit console shows dependencies installing and server starting without exceptions.
- Confirm your client can connect:
  - URL: `https://your-repl-domain/sse`
  - Header: `Authorization: Bearer <MCP_API_KEY>`
- Call `health_check` tool from your client to verify both Pinecone and embedding reachability.

## Troubleshooting

- **Dependencies not installing**:
  - Check that `replit.nix`, `install.sh`, and `.replit` files are present
  - Try running `pip install -r mcp-server/requirements.txt` manually in the shell

- **401 Unauthorized**:
  - Ensure your client sends `Authorization: Bearer <MCP_API_KEY>`
  - Confirm MCP_API_KEY in client matches the Replit Secret value

- **404 Not Found on /sse**:
  - Ensure you launched with `--cloud`
  - Verify URL spelling and that the Repl is running

- **Pinecone "index not found" or "invalid region"**:
  - Check PINECONE_INDEX and PINECONE_ENVIRONMENT in Replit Secrets
  - Ensure your Pinecone Serverless index exists in `us-west1-gcp-free` or set the correct region

- **OpenAI authentication errors**:
  - Confirm OPENAI_API_KEY is set
  - If using OPENAI_BASE_URL, ensure it points to a compatible endpoint

## Reference

- Server entry: [mcp-server/mcp_pinecone_server.py](mcp-server/mcp_pinecone_server.py)
- Config: [mcp-server/mcp_config.py](mcp-server/mcp_config.py)
- Pinecone helpers: [mcp-server/pinecone_client.py](mcp-server/pinecone_client.py)
- Requirements: [mcp-server/requirements.txt](mcp-server/requirements.txt)
- Installation: [install.sh](../install.sh)
- System deps: [replit.nix](../replit.nix)
- Example tests: [scripts/test_mcp_tools.py](scripts/test_mcp_tools.py)