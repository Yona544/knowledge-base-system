---
title: Ace Adsgetfieldnum
slug: ace_adsgetfieldnum
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetfieldnum.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: dae63803de62952702d0a8033dfb13e3043255d2
---

# Ace Adsgetfieldnum

AdsGetFieldNum

AdsGetFieldNum

Advantage Client Engine

| AdsGetFieldNum  Advantage Client Engine |  |  |  |  |

Retrieves the number of a field in a table

Syntax

| UNSIGNED32 | AdsGetFieldNum (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusNum); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pusNum (O) | Return field number corresponding to given name. |

Remarks

The field number is an index in the table of fields from first to last, with the index of the first field being 1.

When using SQL statements the table handle parameter can be replaced with a cursor handle. In this situation AdsGetFieldNumber will return the column number in the rowset.

Example

[Click Here](ace_examples.md#adsgetfieldnumexample)

See Also

[AdsGetFieldName](ace_adsgetfieldname.md)

[AdsGetNumFields](ace_adsgetnumfields.md)
