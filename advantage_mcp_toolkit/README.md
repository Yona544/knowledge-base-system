# Advantage CHM → MCP Knowledge Toolkit

This kit helps you turn a Windows **.CHM** help file into an **MCP-ready** knowledge folder.

## Step 1 — Decompile the `.chm` on Windows (one command)

Open **Command Prompt** and run (adjust paths):

```
hh.exe -decompile "C:\temp\advantage_help" "C:\path\to\advantage.chm"
```

This produces HTML files under `C:\temp\advantage_help`.

> Tip: you can also right‑click the CHM → *Open With* → *HTML Help Executable (hh.exe)*; the `-decompile` switch is part of Windows HTML Help.

## Step 2 — Use this toolkit to convert HTML → Markdown and (optionally) JSONL chunks

### Option A: Convert to Markdown folder only (best for most MCP knowledge servers)

```
python convert_help_to_md.py --in "C:\temp\advantage_help" --out ".\advantage-md"
```

### Option B: Also build `chunks.jsonl` for external vector/RAG pipelines

```
python convert_help_to_md.py --in "C:\temp\advantage_help" --out ".\advantage-md" --make-jsonl
```

This will create:
- `advantage-md/` mirrored folder of cleaned `.md` files
- `advantage-md/index.jsonl` (one document per page; metadata)
- `advantage-md/chunks.jsonl` (only if `--make-jsonl` is set; ~2k‑char chunks)

## Step 3 — Hook into MCP

### 3A. *Filesystem* server (browse/read Markdown)
Add this to your MCP client config (example `mcp.json`):
```jsonc
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./advantage-md"],
      "alwaysAllow": ["list_directory", "read_text_file"],
      "disabled": false
    }
  }
}
```

### 3B. *Knowledge* server with semantic search (recommended)
Install a Knowledge Base MCP server that indexes `.md` files (e.g., `@jeanibarz/knowledge-base-mcp-server`). 
Point it at the directory you created (see that server’s docs for env vars).

Example (HuggingFace embeddings):
```jsonc
{
  "mcpServers": {
    "kb": {
      "command": "node",
      "args": ["C:/path/to/knowledge-base-mcp-server/build/index.js"],
      "env": {
        "KNOWLEDGE_BASES_ROOT_DIR": "C:/path/to/advantage-md",
        "EMBEDDING_PROVIDER": "huggingface",
        "HUGGINGFACE_API_KEY": "YOUR_KEY",
        "HUGGINGFACE_MODEL_NAME": "sentence-transformers/all-MiniLM-L6-v2"
      },
      "disabled": false
    }
  }
}
```

## Notes
- Internal hyperlinks are rewritten where possible; images/scripts/styles are ignored by default.
- You can tweak chunk size via `--chunk-size` and `--chunk-overlap`.
- For large docs, prefer the knowledge server option for accurate retrieval.
