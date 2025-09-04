---
title: Master Go Top Index
slug: master_go_top_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_go_top_index.htm
source: Advantage CHM
tags:
  - master
checksum: ac55d31e6cfcac487c51a5db125618a8358becbc
---

# Master Go Top Index

Go Top (First, MoveFirst) when a Scope is Set

Go Top (First, MoveFirst) when a Scope is Set

Advantage Concepts

| Go Top (First, MoveFirst) when a Scope is Set  Advantage Concepts |  |  |  |  |

With an index scope set, a Go Top operation causes a Seek for the index key) Jones to occur, in a single operation. A Go Top with an index scope set is very fast.

With a record filter set, a Go Top first goes to the top of the index (the Abbot key, for instance). Then a series of sequential skips occur in the index until the first Jones key is found. The number of skips depends on the number of keys in the index between Abbot and Jones. Therefore, many operations may occur. A Go Top with an index scope is extremely fast relative to a traditional record filter.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.md)
