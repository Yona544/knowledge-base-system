---
title: Dotnet Adsconnection Setcursorcache
slug: dotnet_adsconnection_setcursorcache
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_setcursorcache.htm
source: Advantage CHM
tags:
  - dotnet
checksum: b92b06a27966a6ba88d04343b8b9d93fbeaefe62
---

# Dotnet Adsconnection Setcursorcache

AdsConnection.SetCursorCache

AdsConnection.SetCursorCache

Advantage .NET Data Provider

| AdsConnection.SetCursorCache  Advantage .NET Data Provider |  |  |  |  |

Provides caching of open cursors.

public static void SetCursorCache ( int iNumCursors );

Remarks

SetCursorCache allows configuration of the number of open cursors being cached on the Advantage server. The default number of open tables that are cached is 25.

Caching open cursors allows cursor closes to be cached in order for subsequent SELECTS to occur faster. When a table is closed with the cursor cache greater than zero results in the cursor appearing closed to an application, but still open on the Advantage server. A subsequent AdsCommand execution will return very quickly because the server already has the cursor open. However, if the access rights for a statement handle on a cached cursor are different than those it was originally created with, the Advantage Client Engine will close the cursor and reopen it with the changed access rights.

This setting affects all base tables used in queries including queries that result in live (dynamic) cursors and static cursors. For example, the query "SELECT \* FROM table1 WHERE id=5" produces a live cursor. If cursor caching is turned on, then subsequent executions of queries that reference table1 will be faster because table1 will be held open on the server. A query such as "SELECT \* FROM table1, table2 WHERE table1.id=table2.id" produces a static cursor. With cursor caching turned on, both table1 and table2 will be held open by the server. The temporary (static) table produced by the query is not cached open; it is closed and deleted as soon as the cursor is closed.

SetCursorCache is a global setting that affects the behavior of the entire application.

See Also

[SetTableCache](dotnet_adsconnection_settablecache.md)
