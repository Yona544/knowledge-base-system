---
title: Ade Locktable
slug: ade_locktable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_locktable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ffcf07e20ecae617d7a297d35f841de04cb62965
---

# Ade Locktable

LockTable

TAdsTable.LockTable

Advantage TDataSet Descendant

| TAdsTable.LockTable  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Locks the table.

Syntax

procedure LockTable;

Description

Call LockTable to lock a table and prevent other applications from placing any locks on this table. Other tables in the same application will be locked out because each table has its own unique table handle.

See Also

[AdsLockTable](ade_adslocktable.md)
