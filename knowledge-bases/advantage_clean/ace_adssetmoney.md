---
title: Ace Adssetmoney
slug: ace_adssetmoney
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetmoney.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2e8fe757e11472704024118f7a7cd3d765f291cd
---

# Ace Adssetmoney

AdsSetMoney

AdsSetMoney

Advantage Client Engine

| AdsSetMoney  Advantage Client Engine |  |  |  |  |

Stores the given Money value in the given field.

Syntax

| UNSIGNED32 | AdsSetMoney (ADSHANDLE hObj, UNSIGNED8 \*pucFieldName,  SIGNED64 qMoney); |

Parameters

| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFieldName (I) | Name of field to set. |
| qMoney (I) | Money value to store in the field. |

Remarks

AdsSetMoney sets the money value for a given Money field. Keep in mind the value given to AdsSetMoney will be interpreted as an integer with 4 implied decimals, (i.e., to set a field to $19.95, the Money value would be 199500.) To set actual currency values (i.e., 19.95), use [AdsSetDouble](ace_adssetdouble.md) or [AdsSetField](ace_adssetfield.md). [AdsSetLongLong](ace_adssetlonglong.md), [AdsSetLong](ace_adssetlong.md), or [AdsSetShort](ace_adssetshort.md) could also be used although these functions would round the value to the nearest whole number.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.md) and [AdsBuildRawKey](ace_adsbuildrawkey.md).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.md). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE cost > :Amount" );

AdsSetMoney( hStatement, "Amount", 754900 );

AdsExecuteSQL( hStatement, &hCursor);

See Also

[AdsGetMoney](ace_adsgetmoney.md)

[AdsSetField](ace_adssetfield.md)

[AdsSetLongLong](ace_adssetlonglong.md)

[AdsSetDouble](ace_adssetdouble.md)
