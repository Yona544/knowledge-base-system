# Team Setup: Pinecone KB MCP Server

This guide enables the team to run the MCP server locally (stdio or HTTP SSE) and connect MCP-aware clients.

- Server entry: [mcp-server/mcp_pinecone_server.py](mcp-server/mcp_pinecone_server.py)
- Config: [mcp-server/mcp_config.py](mcp-server/mcp_config.py)
- Pinecone helpers: [mcp-server/pinecone_client.py](mcp-server/pinecone_client.py)
- Requirements: [mcp-server/requirements.txt](mcp-server/requirements.txt)
- Replit deployment: [mcp-server/deploy_replit.md](mcp-server/deploy_replit.md)
- Repo README: [mcp-server/README.md](mcp-server/README.md)

## Prerequisites

- Python 3.10+ recommended
- pip and virtualenv (optional but recommended)
- Active API keys:
  - OPENAI_API_KEY
  - PINECONE_API_KEY
- Pinecone Serverless index provisioned (default region: us-west1-gcp-free)
- Knowledge base text under `knowledge-bases/` (namespaces map to Pinecone namespaces)

## Environment variables

Set as OS env vars or in a local `.env` (keep secrets out of VCS):

- OPENAI_API_KEY
- PINECONE_API_KEY
- PINECONE_INDEX (default: knowledge-base-index)
- PINECONE_ENVIRONMENT (default: us-west1-gcp-free)
- MCP_API_KEY (required for HTTP SSE; clients send Authorization: Bearer)
- MCP_SERVER_PORT (default: 3000)
- EMBED_MODEL (default: text-embedding-3-small)
- LLM_MODEL (default: gpt-4o-mini)
- OPENAI_BASE_URL (optional global; can also be overridden per call)

## Install dependencies

- Create/activate a virtualenv (optional).
- Install:
  - `pip install -r mcp-server/requirements.txt`

## Run modes

Two supported run modes:

1) Local stdio (no HTTP):
- Command:
  - `python mcp-server/mcp_pinecone_server.py`
- Use this when your MCP client supports stdio transport to a local process.

2) HTTP SSE (cloud/local HTTP with Bearer auth):
- Command:
  - `python mcp-server/mcp_pinecone_server.py --cloud --port 3000`
- Clients connect to `http://localhost:3000/sse` (or your cloud URL) using header:
  - `Authorization: Bearer ${MCP_API_KEY}`

## Client configuration (Windsurf MCP)

Example SSE config:

```
{
  "mcpServers": {
    "pinecone-kb-sse": {
      "type": "sse",
      "url": "http://localhost:3000/sse",
      "headers": {
        "Authorization": "Bearer ${env:MCP_API_KEY}"
      }
    }
  }
}
```

Notes:
- Replace `http://localhost:3000/sse` with your cloud URL (see [mcp-server/deploy_replit.md](mcp-server/deploy_replit.md) for Replit).
- Ensure your local environment exports the same MCP_API_KEY value used by the server.

## Testing the tools locally

Quick validator script (invokes tool handlers directly):

- Run:
  - `python scripts/test_mcp_tools.py`
- Script path: [scripts/test_mcp_tools.py](scripts/test_mcp_tools.py)
- Behavior:
  - Calls health_check, list_knowledge_bases, get_repository_stats
  - Validates search_kb default k=8
  - Calls get_doc from a search hit
  - Calls synthesize_answer with topk=6
  - Calls answer_knowledge with default k=8
  - Calls list_recent_updates

Optional: set `TEST_REPOSITORY` env var to force a specific repository (namespace).

## Per-call overrides (no redeploy)

To switch endpoints/models/index at runtime, pass optional fields in tool requests:

- indexOverride: override Pinecone index
- repository: Pinecone namespace to query
- embedModel: embedding model override
- llmModel: chat model override (synthesis/answer)
- openaiBaseUrl: OpenAI-compatible base URL override

These apply to:
- search_kb
- synthesize_answer
- answer_knowledge

## Troubleshooting

- 401 Unauthorized on SSE:
  - Ensure client sends `Authorization: Bearer ${MCP_API_KEY}`
  - Verify MCP_API_KEY matches the server-side environment

- Pinecone errors (index/region):
  - Confirm PINECONE_INDEX and PINECONE_ENVIRONMENT
  - Ensure a Serverless index exists in the specified region

- OpenAI errors:
  - Confirm OPENAI_API_KEY
  - If using OPENAI_BASE_URL, ensure the endpoint is compatible and reachable

- No results:
  - Verify the repository (namespace) exists in Pinecone and your local `knowledge-bases/` is aligned
  - Try `search_kb` with `repository` set explicitly

## References

- Server: [mcp-server/mcp_pinecone_server.py](mcp-server/mcp_pinecone_server.py)
- Config: [mcp-server/mcp_config.py](mcp-server/mcp_config.py)
- Pinecone helpers: [mcp-server/pinecone_client.py](mcp-server/pinecone_client.py)
- Requirements: [mcp-server/requirements.txt](mcp-server/requirements.txt)
- Replit deploy: [mcp-server/deploy_replit.md](mcp-server/deploy_replit.md)
- Local validator: [scripts/test_mcp_tools.py](scripts/test_mcp_tools.py)