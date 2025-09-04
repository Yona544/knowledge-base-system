---
title: Ace Adsgetmoney
slug: ace_adsgetmoney
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetmoney.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b0ab4e0cc3185474d5493ba518b508f7b4f9d73d
---

# Ace Adsgetmoney

AdsGetMoney

AdsGetMoney

Advantage Client Engine

| AdsGetMoney  Advantage Client Engine |  |  |  |  |

Retrieves the Money value from the given field.

Syntax

| UNSIGNED32 | AdsGetMoney (ADSHANDLE hObj, UNSIGNED8 \*pucFieldName,  SIGNED64 \*pqMoney); |

Parameters

| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFieldName (I) | Name of field to get. |
| pqMoney (O) | Return the value. |

Remarks

AdsGetMoney retrieves the value stored in a money field. The value is returned as an integer with four implied decimal digits of precision, (i.e., an actual value of 19.95 would be returned as 199500.) To get the real value of a money field, use [AdsGetField](ace_adsgetfield.md) or [AdsGetDouble](ace_adsgetdouble.md). [AdsGetLongLong](ace_adsgetlonglong.md), [AdsGetLong](ace_adsgetlong.md), or [AdsGetShort](ace_adsgetshort.md) could also be used although these functions would round the value to the nearest whole number.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc

Example 1

AdsPrepareSQL( hStatement,

"SELECT cost FROM test WHERE cost > 100.00" );

AdsExecuteSQL( hStatement, &hCursor);

AdsGetMoney( hCursor, "cost", &qMoneyValue );

See Also

[AdsSetMoney](ace_adssetmoney.md)

[AdsGetField](ace_adsgetfield.md)

[AdsGetLongLong](ace_adsgetlonglong.md)

[AdsGetDouble](ace_adsgetdouble.md)
