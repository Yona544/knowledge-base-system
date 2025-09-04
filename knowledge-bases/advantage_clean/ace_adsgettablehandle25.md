---
title: Ace Adsgettablehandle25
slug: ace_adsgettablehandle25
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablehandle25.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d83905b01db956be8ffc77b9744f7885c2278204
---

# Ace Adsgettablehandle25

AdsGetTableHandle25

AdsGetTableHandle25

Advantage Client Engine

| AdsGetTableHandle25  Advantage Client Engine |  |  |  |  |

Searches through the list of open tables on the specified connection to find the table with the given filename

Syntax

UNSIGNED32 AdsGetTableHandle25 ( ADSHANDLE hConnect, UNSIGNED8 \*pucName,

ADSHANDLE \*phTable );

Parameters

| hConnect (I) | Connection to search for the open table. If this parameter is zero, all connections are searched. |
| pucName (I) | Table name. The given name will be resolved to full path using the same algorithm as [AdsOpenTable](ace_adsopentable.md). |
| phTable (O) | Handle of the table if found. |

Special Return Codes

| AE\_TABLE\_CACHED | This table is marked as closed after a call to [AdsCloseTable](ace_adsclosetable.md), but the close was cached. |
| AE\_NOT\_FOUND | A handle to the table was not found. |

Remarks

The Advantage Client Engine will attempt to resolve the given name (pucName) to a fully qualified path name and search for a matching filename.

This API is similar to [AdsGetTableHandle](ace_adsgettablehandle.md) except that a connection handle can be specified to limit the scope of the search. If zero is specified as the connection handle when calling this API, the behavior is identical to AdsGetTableHandle API.

Example

ulRetCode = AdsGetTableHandle25( hConn, "Table1", &hTable );

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableFilename](ace_adsgettablefilename.md)

[AdsGetTableAlias](ace_adsgettablealias.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)
