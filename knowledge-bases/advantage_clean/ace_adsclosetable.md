---
title: Ace Adsclosetable
slug: ace_adsclosetable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsclosetable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 951795f865fb758f37a599696bb3650f6b6e8e43
---

# Ace Adsclosetable

AdsCloseTable

AdsCloseTable

Advantage Client Engine

| AdsCloseTable  Advantage Client Engine |  |  |  |  |

Closes the given table

Syntax

| UNSIGNED32 | AdsCloseTable (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor to close. |

Remarks

AdsCloseTable is used to close an open table and any associated index or memo files. Any locks held on the table are released, and changes are flushed when a table is closed. If the close is cached, however, changes are flushed and implicit locks are released. Explicit locks remain if any are held when the table was closed.

The Advantage Client Engine will NOT disconnect from the server when the last table is closed. Settings specified by [AdsCacheOpenTables](ace_adscacheopentables.md) will be obeyed.

When using SQL cursors the table handle parameter can be replaced with a cursor handle. In this situation AdsCloseTable will close the cursor and all of its associated memory. After closing a cursor the cursor handle can then be reused in a new call to either AdsExecuteSQL or AdsExecuteSQLDirect.

Note This function is legal in a transaction, but its behavior varies. If the table, memo, and indexes associated with the table were never modified, then the files will be closed. If they were modified in any way, then the files will be cached closed. The file will not actually be closed until the transaction is committed or rolled back.

Example

[Click Here](ace_examples.md#adsclosetableexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsDisconnect](ace_adsdisconnect.md)

[AdsCloseAllTables](ace_adsclosealltables.md)

[AdsCacheOpenTables](ace_adscacheopentables.md)

[AdsExecuteSQL](ace_adsexecutesql.md)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.md)

[AdsCloseCachedTables](ace_adsclosecachedtables.md)
