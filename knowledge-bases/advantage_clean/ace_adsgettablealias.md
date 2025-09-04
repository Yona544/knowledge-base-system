---
title: Ace Adsgettablealias
slug: ace_adsgettablealias
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablealias.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d08f4ef502e124409e9a65a17b14299a5c8fbd22
---

# Ace Adsgettablealias

AdsGetTableAlias

AdsGetTableAlias

Advantage Client Engine

| AdsGetTableAlias  Advantage Client Engine |  |  |  |  |

Retrieves the alias associated with the given table handle

Syntax

| UNSIGNED32 | AdsGetTableAlias (ADSHANDLE hTable,  UNSIGNED8 \*pucAlias,  UNSIGNED16 \*pusLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucAlias (O) | Return the alias in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetTableAlias retrieves the alias associated with the table during the open or create. If no alias was specified when the table was opened, the Advantage Client Engine generates the alias from the base filename of the table.

If the table in question is in an Advantage Data Dictionary, AdsGetTableAlias will return the name of the table object in the dictionary.

Example

[Click Here](ace_examples.md#adsgettablealiasexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableFilename](ace_adsgettablefilename.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)
