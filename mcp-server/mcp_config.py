#!/usr/bin/env python3
# mcp-server/mcp_config.py
# Centralized configuration and helpers for the Pinecone KB MCP server.

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class MCPConfig:
    openai_api_key: Optional[str]
    pinecone_api_key: Optional[str]
    pinecone_environment: str
    pinecone_index: str
    embed_model: str
    llm_model: str
    mcp_server_port: int
    mcp_api_key: Optional[str]
    openai_base_url: Optional[str] = None  # optional override for custom endpoints
    pinecone_host: Optional[str] = None    # optional serverless host override


def _getenv(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    if v is None:
        return default
    return v


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def repo_root(repository: Optional[str]) -> Path:
    """
    Resolve a repository root under knowledge-bases/.
    Preference order:
      1) knowledge-bases/{repository}_clean
      2) knowledge-bases/{repository}
    Fallback: knowledge-bases/advantage_clean
    """
    kb_root = project_root() / "knowledge-bases"
    if not repository:
        return kb_root / "advantage_clean"

    candidates = [kb_root / f"{repository}_clean", kb_root / repository]
    for p in candidates:
        if p.exists():
            return p

    # Fallback
    return kb_root / "advantage_clean"


def load_config() -> MCPConfig:
    """
    Load configuration from environment with sensible defaults aligned to the MD specs.
    """
    # Env resolution with spec-aligned defaults
    pine_env = (
        _getenv("PINECONE_ENVIRONMENT")
        or _getenv("PINECONE_ENV")
        or "us-west1-gcp-free"
    )
    pine_index = (
        _getenv("PINECONE_INDEX")
        or _getenv("PINECONE_INDEX_NAME")
        or "advantage-v2"
    )
    mcp_port = int(_getenv("MCP_SERVER_PORT", "3000") or "3000")  
    embed_model = _getenv("EMBED_MODEL", "text-embedding-3-small") or "text-embedding-3-small"
    llm_model = _getenv("LLM_MODEL", "gpt-4o-mini") or "gpt-4o-mini"
    openai_base_url = _getenv("OPENAI_BASE_URL") or _getenv("OPENAI_API_BASE")
    pine_host = _getenv("PINECONE_HOST")

    return MCPConfig(
        openai_api_key=_getenv("OPENAI_API_KEY"),
        pinecone_api_key=_getenv("PINECONE_API_KEY"),
        pinecone_environment=pine_env,
        pinecone_index=pine_index,
        embed_model=embed_model,
        llm_model=llm_model,
        mcp_server_port=mcp_port,
        mcp_api_key=_getenv("MCP_API_KEY"),
        openai_base_url=openai_base_url,
        pinecone_host=pine_host,
    )


def effective_index(cfg: MCPConfig, index_override: Optional[str]) -> str:
    """
    Select an effective index name, allowing a per-request override passed by tools.
    """
    return (index_override or cfg.pinecone_index).strip()