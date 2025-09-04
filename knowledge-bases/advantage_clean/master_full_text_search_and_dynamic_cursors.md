---
title: Master Full Text Search And Dynamic Cursors
slug: master_full_text_search_and_dynamic_cursors
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_and_dynamic_cursors.htm
source: Advantage CHM
tags:
  - master
checksum: b85569e2a3b6af72cc83beb02e7843a43e569c2d
---

# Master Full Text Search And Dynamic Cursors

Full Text Search and Dynamic Cursors

Full Text Search and Dynamic Cursors

Advantage Concepts

| Full Text Search and Dynamic Cursors  Advantage Concepts |  |  |  |  |

By default, Advantage creates dynamic cursors. When one client makes an update to a table, other clients cursors (result sets) are updated as appropriate based on the record changes. See [Use Dynamic Cursors](master_use_dynamic_cursors.md) for more information. When the CONTAINS() scalar function is used, however, Advantage will not dynamically update cursor memberships. The cost of evaluating the conditions on memo and BLOB fields would be prohibitively expensive.
