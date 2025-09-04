AdsGetLongLong




Advantage Database Server 12  

AdsGetLongLong

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetLongLong  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetLongLong Advantage Client Engine ace\_Adsgetlonglong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetLongLong  Advantage Client Engine |  |  |  |  |

Retrieves the signed long long integer from the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetLongLong (ADSHANDLE hObj, UNSIGNED8 \*pucFldName,  SIGNED64 \*pqValue); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to get. |
| pqValue (O) | Return the value. |

Remarks

AdsGetLongLong returns the signed long long (SIGNED64) value stored in the numeric, long integer, integer, short integer, double, CurDouble, auto-increment, RowVersion, or Money field.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

AdsPrepareSQL( hStatement,

"SELECT FROM test WHERE cost > 100000000" );

AdsExecuteSQL( hStatement, &hCursor);

AdsGetLongLong( hCursor, "cost", &qValue );

See Also

[AdsGetField](ace_adsgetfield.htm)

[AdsGetLong](ace_adsgetlong.htm)

[AdsSetLongLong](ace_adssetlonglong.htm)