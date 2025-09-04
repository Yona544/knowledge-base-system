#!/usr/bin/env python3
# mcp-server/pinecone_client.py
# Thin helpers around Pinecone Python client for the MCP server.

from __future__ import annotations

from typing import Any, Dict, List, Optional
import os  # added to read host overrides from environment if needed

from pinecone import Pinecone

from mcp_config import MCPConfig


def get_pc(cfg: MCPConfig, api_key_override: Optional[str] = None) -> Pinecone:
    """
    Construct a Pinecone client using an override API key if provided,
    otherwise fall back to the configured key.
    """
    api_key = api_key_override or cfg.pinecone_api_key
    if not api_key:
        raise RuntimeError("Missing PINECONE_API_KEY")
    # Pinecone v5 client does not require environment during client construction
    return Pinecone(api_key=api_key)


def get_index(cfg: MCPConfig, index_name: str, api_key_override: Optional[str] = None, host_override: Optional[str] = None):
    pc = get_pc(cfg, api_key_override=api_key_override)
    host = host_override or cfg.pinecone_host
    if host:
        return pc.Index(index_name, host=host)
    return pc.Index(index_name)


def describe_index_stats_safe(index) -> Dict[str, Any]:
    """
    Safe wrapper around describe_index_stats that normalizes return shape to dict.
    """
    try:
        stats = index.describe_index_stats()
        # Some SDK versions return Typed objects; coerce to dict if necessary
        if hasattr(stats, "to_dict"):
            return stats.to_dict()  # type: ignore[attr-defined]
        if isinstance(stats, dict):
            return stats
        # Fallback: try best-effort
        return dict(stats)
    except Exception as e:
        raise RuntimeError(f"Failed to describe index stats: {e}") from e


def list_namespaces(cfg: MCPConfig, index_name: str, api_key_override: Optional[str] = None, host_override: Optional[str] = None) -> List[str]:
    """
    Return a list of namespace names in the index.
    """
    index = get_index(cfg, index_name, api_key_override=api_key_override, host_override=host_override)
    stats = describe_index_stats_safe(index)
    namespaces = (stats or {}).get("namespaces") or {}
    # Pinecone sometimes uses dict with namespace -> {vectorCount: int}
    return sorted(list(namespaces.keys()))


def get_namespace_stats(
    cfg: MCPConfig,
    index_name: str,
    namespace: Optional[str] = None,
    api_key_override: Optional[str] = None,
    host_override: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Return index-wide stats, or per-namespace if provided.
    """
    index = get_index(cfg, index_name, api_key_override=api_key_override, host_override=host_override)
    stats = describe_index_stats_safe(index)
    if namespace:
        namespaces = (stats or {}).get("namespaces") or {}
        return namespaces.get(namespace, {"vectorCount": 0})
    return stats


def health_check(cfg: MCPConfig, index_name: str, api_key_override: Optional[str] = None, host_override: Optional[str] = None) -> Dict[str, Any]:
    """
    Perform a simple health check by calling describe_index_stats.
    """
    try:
        _ = list_namespaces(cfg, index_name, api_key_override=api_key_override, host_override=host_override)
        return {"ok": True, "index": index_name, "message": "Pinecone reachable"}
    except Exception as e:
        return {"ok": False, "index": index_name, "error": str(e)}