---
title: Ace Adsgetnumfields
slug: ace_adsgetnumfields
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetnumfields.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: eb94cf0e583e0b89fb7102b0c0e3bc0e864c4682
---

# Ace Adsgetnumfields

AdsGetNumFields

AdsGetNumFields

Advantage Client Engine

| AdsGetNumFields  Advantage Client Engine |  |  |  |  |

Retrieves the number of fields in the given table

Syntax

| UNSIGNED32 | AdsGetNumFields (ADSHANDLE hTable,  UNSIGNED16 \*pusCount); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusCount (O) | Return field count for given table. |

Remarks

The returned field count does not include the deleted byte in DBF tables.

When using SQL statements the table handle parameter can be replaced with a cursor handle. In this situation AdsGetNumFields will return the number of columns in the rowset.

Example

[Click Here](ace_examples.md#adsgetnumfieldsexample)

See Also

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetFieldName](ace_adsgetfieldname.md)
