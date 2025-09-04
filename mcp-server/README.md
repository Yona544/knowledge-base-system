# Pinecone KB MCP Server

This directory provides a Python MCP server that exposes search and answer tools over stdio (local) and HTTP SSE (cloud).

- Server entry: [mcp-server/mcp_pinecone_server.py](mcp-server/mcp_pinecone_server.py)
- Config: [mcp-server/mcp_config.py](mcp-server/mcp_config.py)
- Pinecone helpers: [mcp-server/pinecone_client.py](mcp-server/pinecone_client.py)
- Requirements: [mcp-server/requirements.txt](mcp-server/requirements.txt)

## Tools

- list_knowledge_bases
- get_repository_stats
- list_recent_updates
- search_kb
- get_doc
- synthesize_answer
- answer_knowledge (wrapper over synthesis, default k=8)

## Environment variables

- OPENAI_API_KEY
- PINECONE_API_KEY
- PINECONE_INDEX (default: knowledge-base-index)
- PINECONE_ENVIRONMENT (default: us-west1-gcp-free)
- MCP_API_KEY (required for HTTP SSE; clients must send Authorization: Bearer)
- MCP_SERVER_PORT (default: 3000)
- EMBED_MODEL (default: text-embedding-3-small)
- LLM_MODEL (default: gpt-4o-mini)
- OPENAI_BASE_URL (optional override; can also be set per call with `openaiBaseUrl`)

## Run locally

- Install deps:
  - `pip install -r mcp-server/requirements.txt`
- Stdio mode:
  - `python mcp-server/mcp_pinecone_server.py`
- HTTP SSE mode (Bearer auth):
  - `python mcp-server/mcp_pinecone_server.py --cloud --port 3000`
  - Clients connect with `Authorization: Bearer ${MCP_API_KEY}`

## Replit deployment

- Create a Python Repl and include the `mcp-server/` folder
- Set Secrets:
  - OPENAI_API_KEY
  - PINECONE_API_KEY
  - MCP_API_KEY
  - PINECONE_INDEX=knowledge-base-index
  - PINECONE_ENVIRONMENT=us-west1-gcp-free
- Run command:
  - `python mcp-server/mcp_pinecone_server.py --cloud --port 3000`
- Use the public Replit URL with your MCP client and pass the Authorization header

## Per-call overrides

To change endpoints or models on the fly (no redeploy), pass optional fields to the tools:

- indexOverride: override `PINECONE_INDEX` for this call
- repository: Pinecone namespace (repo) to target
- embedModel: override embedding model
- llmModel: override chat model (synthesis)
- openaiBaseUrl: override OpenAI base URL (e.g., for a reverse proxy)

Applies to:
- search_kb
- synthesize_answer
- answer_knowledge

## Security

- HTTP SSE requires `Authorization: Bearer ${MCP_API_KEY}`
- Share the MCP_API_KEY only with trusted users; anyone with the key can call the server tools

## Notes

- The server expects your knowledge-base content under `knowledge-bases/` and resolves repository roots using `mcp_config.repo_root`.
- Use Pinecone serverless index in the configured region. Index creation/ingest is handled elsewhere in the repo.