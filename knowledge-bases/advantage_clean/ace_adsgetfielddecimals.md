---
title: Ace Adsgetfielddecimals
slug: ace_adsgetfielddecimals
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetfielddecimals.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5e97b58a5467dd55a8c8da885c5fcfa83bac450f
---

# Ace Adsgetfielddecimals

AdsGetFieldDecimals

AdsGetFieldDecimals

Advantage Client Engine

| AdsGetFieldDecimals  Advantage Client Engine |  |  |  |  |

Retrieves decimals (for numerics) of a field in a table

Syntax

| UNSIGNED32 | AdsGetFieldDecimals (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusDecimals); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pusDecimals (O) | Return field decimals. |

Remarks

AdsGetFieldDecimals returns the number of digits of decimal precision in the field to the right of the decimal point in a numeric field.

Example

[Click Here](ace_examples.md#adsgetfielddecimalsexample)

See Also

[AdsGetFieldLength](ace_adsgetfieldlength.md)

[AdsGetFieldName](ace_adsgetfieldname.md)

[AdsGetFieldNum](ace_adsgetfieldnum.md)

[AdsGetFieldType](ace_adsgetfieldtype.md)

[AdsGetNumFields](ace_adsgetnumfields.md)
