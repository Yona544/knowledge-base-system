---
title: Ace Adsgetshort
slug: ace_adsgetshort
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetshort.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f37a45e61144365de06e9cbbabf80a52cb006b0d
---

# Ace Adsgetshort

AdsGetShort

AdsGetShort

Advantage Client Engine

| AdsGetShort  Advantage Client Engine |  |  |  |  |

Retrieves the short (two byte) integer value from the given field

Syntax

| UNSIGNED32 | AdsGetShort (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  SIGNED16 \*psValue); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| psValue (O) | Return the value. |

Remarks

AdsGetShort returns the signed short (two byte) value stored in the numeric, long integer, integer, short integer, double, CurDouble, Money, RowVersion, or auto-increment field. It is possible to either overflow the value or lose decimal precision by using this function. If more precision is desired, use [AdsGetDouble](ace_adsgetdouble.md). If AdsGetShort is used to retrieve a Money field, the four decimal digits will be rounded to the nearest whole number.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_more_examples.md#adsgetshortexample)

See Also

[AdsGetField](ace_adsgetfield.md)

[AdsSetShort](ace_adssetshort.md)
