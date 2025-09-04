---
title: Master Seek Index
slug: master_seek_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_seek_index.htm
source: Advantage CHM
tags:
  - master
checksum: f776483e86bcc8040a2817b91d1c22be07465c87
---

# Master Seek Index

Seek (FindKey, FindNearest, GotoKey, GotoNearest) when a Scope is Set

Seek (FindKey, FindNearest, GotoKey, GotoNearest) when a Scope is Set

Advantage Concepts

| Seek (FindKey, FindNearest, GotoKey, GotoNearest) when a Scope is Set  Advantage Concepts |  |  |  |  |

If the key) being Seeked is within the index scope or record filter boundaries (the Nelson key, for instance), then index scope and record filter performance is identical.

If the key being Seeked is before the top index scope or record filter boundary (the Brown key, for instance), index scopes are much faster than traditional record filters. With index scopes, a Seek to the top of the scope (the first Jones key) or an immediate repositioning to the end of file will occur, depending if Softseek is set. With traditional record filters, a series of skips will be performed (from the Brown key to the Jones key) before the Softseek setting is accounted for.

If the key being Seeked is after the bottom index scope or record filter boundary (the Smith key, for instance), then index scopes are once again faster than traditional record filters. With index scopes, an immediate repositioning to the end of file will occur. With record filters, a series of skips will be performed (starting at the Smith key) until the end of file is reached.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.md)
