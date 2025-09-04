---
title: Dotnet Adsconnection Settablecache
slug: dotnet_adsconnection_settablecache
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_settablecache.htm
source: Advantage CHM
tags:
  - dotnet
checksum: a8a1169251d93775321e29603b2b71165733bb5c
---

# Dotnet Adsconnection Settablecache

AdsConnection.SetTableCache

AdsConnection.SetTableCache

Advantage .NET Data Provider

| AdsConnection.SetTableCache  Advantage .NET Data Provider |  |  |  |  |

Provides caching of open tables.

public static void SetTableCache( int iNumTables );

Remarks

SetTableCache allows configuration of the number of open tables being cached on the Advantage server. The default number of open tables that are cached is zero.

Caching open tables allows table closes to be cached in order for subsequent opens to occur faster. When a table is closed with the table cache greater than zero results in the table appearing closed to an application, but still open on the Advantage server. A subsequent open will return very quickly because the server already has the table open. However, if the access rights for an open on a cached table are different than those that it was originally opened with, the Advantage Client Engine will close the table and reopen it with the changed access rights.

Call this method if an application performs multiple opens and closes on the same table. If an application opens tables and leaves them open, table caching provides no additional value.

SetTableCache is a global setting that affects the behavior of the entire application.

See Also

[CloseCachedTables](dotnet_adsconnection_closecachedtables.md)

[SetCursorCache](dotnet_adsconnection_setcursorcache.md)
