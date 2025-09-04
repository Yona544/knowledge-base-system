---
title: Ace Adsgetlong
slug: ace_adsgetlong
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetlong.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9fb20773793f12ceceb21ddabe4d49d8b4276711
---

# Ace Adsgetlong

AdsGetLong

AdsGetLong

Advantage Client Engine

| AdsGetLong  Advantage Client Engine |  |  |  |  |

Retrieves the long integer value from the given field.

Syntax

| UNSIGNED32 | AdsGetLong (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  SIGNED32 \*plValue); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| plValue (O) | Return the value. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF. |

Remarks

AdsGetLong returns the signed long value stored in the numeric, long integer, integer, short integer, double, CurDouble, Money, RowVersion, or auto-increment field. It is possible to either overflow the value or lose decimal precision by using this function. If more range or precision is desired, use [AdsGetDouble](ace_adsgetdouble.md) or [AdsGetLongLong](ace_adsgetlonglong.md). When using this function to retrieve an auto-increment value, be sure to treat the result as an unsigned value. If AdsGetLong is used to retrieve a Money field, the four decimal digits will be rounded to the nearest whole number.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetlongexample)

See Also

[AdsGetField](ace_adsgetfield.md)

[AdsSetLong](ace_adssetlong.md)

[AdsGetLongLong](ace_adsgetlonglong.md)
