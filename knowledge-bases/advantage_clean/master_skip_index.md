---
title: Master Skip Index
slug: master_skip_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_skip_index.htm
source: Advantage CHM
tags:
  - master
checksum: 989bad1057a124ff3c85e59a5a10be2ed4cf9247
---

# Master Skip Index

Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set

Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set

Advantage Concepts

| Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set  Advantage Concepts |  |  |  |  |

Performance of Skips is similar to Seeks. If the Skip occurs within the index scope or record filter boundaries, index scope and record filter performance is identical. If the Skip occurs outside of the index scope or record filter boundaries, index scopes are again much faster than record filters. See the [Seek](master_seek_index.md) section for a full explanation of how Skips work like Seeks when outside the index scope or record filter boundaries.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.md)
