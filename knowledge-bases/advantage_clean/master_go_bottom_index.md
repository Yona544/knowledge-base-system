---
title: Master Go Bottom Index
slug: master_go_bottom_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_go_bottom_index.htm
source: Advantage CHM
tags:
  - master
checksum: 98490e5f22442dd2dda225a6bf24dd6712886da9
---

# Master Go Bottom Index

Go Bottom (Last, MoveLast) when a Scope is Set

Go Bottom (Last, MoveLast) when a Scope is Set

Advantage Concepts

| Go Bottom (Last, MoveLast) when a Scope is Set  Advantage Concepts |  |  |  |  |

With an index scope set, a Go Bottom causes a Seek for the index key) Phillipt (note that it is Phillipt rather than Phillips). Then a negative Skip is performed to position the user on the last of any Phillips keys. Therefore, two operations occur. A Go Bottom with an index scope set is very fast.

With a record filter set, a Go Bottom first goes to the bottom of the index (the Zimmerman key, for instance). Then a series of sequential negative Skips occur in the index until a Phillips key is found. The number of negative Skips depends on the number of keys in the index between Zimmerman and Phillips. Thus, many operations occur. A Go Bottom with an index scope is extremely fast relative to a traditional record filter.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.md)
