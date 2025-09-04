---
title: Ace Adszaptable
slug: ace_adszaptable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adszaptable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fd0ac5275b9927cefb882fecc58a0b9a29049c71
---

# Ace Adszaptable

AdsZapTable

AdsZapTable

Advantage Client Engine

| AdsZapTable  Advantage Client Engine |  |  |  |  |

Removes all records from the table and reindexes it

Syntax

| UNSIGNED32 | AdsZapTable (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table. |

Remarks

AdsZapTable will remove all records from the table and all data from the memo file, and then the Advantage Client Engine will reindex the table. The indexes must be opened during the zap or they will become invalid. This operation requires exclusive access to the table, which is specified during the open. AdsZapTable is illegal in a transaction.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

Example

[Click Here](ace_examples.md#adszaptableexample)

See Also

[AdsPackTable](ace_adspacktable.md)

[AdsOpenTable](ace_adsopentable.md)
