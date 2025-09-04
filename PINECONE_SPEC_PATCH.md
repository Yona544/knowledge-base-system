
# Spec Patch — Pinecone Knowledge Base System
_Last updated: 2025-09-02 18:59:56_

This patch updates the original spec to reflect your latest decisions: hybrid retrieval, file-name-forward metadata, SQL-topic classification, six-part summaries, `top_k=8`, answer tool, and a persistent task ledger.

## 1) Config Changes
### `config/global_config.yaml`
```yaml
pinecone:
  index_name: "knowledge-base-index"
  dimension: 1536

embedding:
  provider: "openai"
  model: "text-embedding-3-small"   # primary (1536 dims)
  batch_size: 100
```

### `config/repository_mapping.yaml`
(No change; ensure folder→namespace mapping remains 1:1.)

## 2) Admin Upload (`admin-tools/`)
- Treat all chunk sizes as **tokens**: `chunk_size=1000`, `chunk_overlap=100`.
- Prepend chunk header line: `[{kb_name} | {file_name} | {sql_topic} | {heading_path}]`.
- Write/update `.kb/status/status.jsonl` and `TASKS.md` per KB.
- Produce `.kb/summaries/{file_stem}.summary6.md` for each MD file.

**Vector metadata additions:**
```
kb_name, namespace, file_path, file_name, title, heading_path, section_id,
sql_topic, language, token_count, sha256, last_modified, keywords, summary6
```

## 3) MCP Server (`mcp-server/`)
Add/modify tools:
- `search_knowledge(query, repository=None, k=8, hybrid=True)` (default hybrid)
- `answer_knowledge(query, repository=None, k=8)`
- `list_recent_updates(repository=None, n=20)`

**Defaults:**
- `k` default: **8**
- Hybrid fusion: dense(16) + lexical(16) → RRF → top 8

**Response format:**
- score, title, kb, file_path, heading_path, 2–3 line snippet, copyable reference

## 4) Hybrid Retrieval Implementation Notes
- Maintain a per-namespace lexical index over `title+headings+text+file_name+sql_topic+keywords+summary6`.
- Use BM25 for lexical; RRF to fuse with dense.
- Optional boosts for `title` and `sql_topic` exact matches.

## 5) SQL Topic Classification
Use the provided heuristic mapping to assign `sql_topic`. Store in metadata and in the chunk header line.

## 6) Evaluation
- Include `eval/gold.jsonl`.
- Report hit@8 and MRR; compare dense vs hybrid.

## 7) Docs Updates (`docs/`)
- **USAGE_EXAMPLES.md**: add examples for `@kb answer` and `@kb status`.
- **TROUBLESHOOTING.md**: resume logic using `.kb/status/status.jsonl`.
- **SETUP_GUIDE.md**: clarify tokens vs characters for chunk_size/overlap.

## 8) Acceptance Criteria
- Index dimension = 1536; hybrid default on; `k=8` default.
- `summary6` is present in metadata and `.kb/summaries/` for every file.
- Task ledger populated and `TASKS.md` generated.
- Answer tool returns concise answers with citations.
