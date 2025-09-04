---
title: Ace Adsgetfieldoffset
slug: ace_adsgetfieldoffset
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetfieldoffset.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4f96449294f0a979eb443bf4da887fa3923b38a4
---

# Ace Adsgetfieldoffset

AdsGetFieldOffset

AdsGetFieldOffset

Advantage Client Engine

| AdsGetFieldOffset  Advantage Client Engine |  |  |  |  |

Retrieves the offset of a field in a table

Syntax

| UNSIGNED32 | AdsGetFieldOffset (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 \*pulOffset); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pulOffset (O) | Return field offset. This is the offset within the record. |

Remarks

Returns the offset of the field in the tables record image in the table.

Example

[Click Here](ace_examples.md#adsgetfieldoffsetexample)

See Also

[AdsGetFieldLength](ace_adsgetfieldlength.md)

[AdsGetFieldName](ace_adsgetfieldname.md)

[AdsGetFieldNum](ace_adsgetfieldnum.md)

[AdsGetNumFields](ace_adsgetnumfields.md)

[AdsGetRecord](ace_adsgetrecord.md)
