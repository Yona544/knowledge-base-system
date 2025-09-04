---
title: Ade Indexdefs
slug: ade_indexdefs
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_indexdefs.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c0a3afc1c2af714bbc282b33ec3f8daee792d048
---

# Ade Indexdefs

IndexDefs

TAdsQuery.IndexDefs

Advantage TDataSet Descendant

| TAdsQuery.IndexDefs  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

With Advantage TDataSet, the IndexDefs property may be used with TAdsQuery exactly as it is used with TAdsTable. If these properties are left blank, the rowset is ordered as defined by the ORDER BY clause of the SQL statement. However, if other indexes are available, one can be selected as the sequence in which the rows are presented.

If the cursor is a live cursor, any index on the original table is available. If the cursor is static, no indexes exist. In either case, you may use the [AdsCreateIndex](ade_adscreateindex.md) method to create new index orders.
