---
title: Ace Adsgettablehandle
slug: ace_adsgettablehandle
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablehandle.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 1e8491ab664db52181998ba9aedf365eb22c86b5
---

# Ace Adsgettablehandle

AdsGetTableHandle

AdsGetTableHandle

Advantage Client Engine

| AdsGetTableHandle  Advantage Client Engine |  |  |  |  |

Searches through the list of open tables to find the table with the given filename

Syntax

| UNSIGNED32 | AdsGetTableHandle (UNSIGNED8 \*pucName,  ADSHANDLE \*phTable); |

Parameters

| pucName (I) | Table name. The given name will be resolved to full path using the same algorithm as [AdsOpenTable](ace_adsopentable.md). |
| phTable (O) | Handle of the table if found. |

Special Return Codes

| AE\_TABLE\_CACHED | This table is marked as closed after a call to [AdsCloseTable](ace_adsclosetable.md), but the close was cached. |
| AE\_NOT\_FOUND | A handle to the table was not found. |

Remarks

The Advantage Client Engine will attempt to resolve the given name (pucName) to a fully qualified path name and search for a matching filename.

To find open table on a specific connection, use [AdsGetTableHandle25](ace_adsgettablehandle25.md).

Example

[Click Here](ace_examples.md#adsgettablehandleexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableFilename](ace_adsgettablefilename.md)

[AdsGetTableAlias](ace_adsgettablealias.md)

[AdsGetTableHandle25](ace_adsgettablehandle25.md)
