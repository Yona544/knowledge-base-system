AdsGetMoney




Advantage Database Server 12  

AdsGetMoney

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetMoney  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetMoney Advantage Client Engine ace\_Adsgetmoney Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetMoney  Advantage Client Engine |  |  |  |  |

Retrieves the Money value from the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetMoney (ADSHANDLE hObj, UNSIGNED8 \*pucFieldName,  SIGNED64 \*pqMoney); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFieldName (I) | Name of field to get. |
| pqMoney (O) | Return the value. |

Remarks

AdsGetMoney retrieves the value stored in a money field. The value is returned as an integer with four implied decimal digits of precision, (i.e., an actual value of 19.95 would be returned as 199500.) To get the real value of a money field, use [AdsGetField](ace_adsgetfield.htm) or [AdsGetDouble](ace_adsgetdouble.htm). [AdsGetLongLong](ace_adsgetlonglong.htm), [AdsGetLong](ace_adsgetlong.htm), or [AdsGetShort](ace_adsgetshort.htm) could also be used although these functions would round the value to the nearest whole number.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc

Example 1

AdsPrepareSQL( hStatement,

"SELECT cost FROM test WHERE cost > 100.00" );

AdsExecuteSQL( hStatement, &hCursor);

AdsGetMoney( hCursor, "cost", &qMoneyValue );

See Also

[AdsSetMoney](ace_adssetmoney.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsGetLongLong](ace_adsgetlonglong.htm)

[AdsGetDouble](ace_adsgetdouble.htm)