AdsSetLongLong




Advantage Database Server 12  

AdsSetLongLong

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetLongLong  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetLongLong Advantage Client Engine ace\_Adssetlonglong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetLongLong  Advantage Client Engine |  |  |  |  |

Stores the given signed long long integer in the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetLongLong (ADSHANDLE hObj, UNSIGNED8 \*pucFldName,  SIGNED64 qValue ); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| qValue (I) | Long long (SIGNED64) value to be stored in table. |

Remarks

AdsSetLongLong can be used to set values for numeric, long integer, integer, short integer, double, CurDouble, RowVersion, and Money fields. If the value of qValue is too large to fit in the field, ADS\_DATA\_TOO\_LONG is returned.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.htm) and [AdsBuildRawKey](ace_adsbuildrawkey.htm).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE total < :MaxAmount" );

AdsSetLongLong( hStatement, "MaxAmount", 10000000000 );

AdsExecuteSQL( hStatement, &hCursor);

See Also

[AdsSetField](ace_adssetfield.htm)

[AdsSetLong](ace_adssetlong.htm)

[AdsSetDouble](ace_adssetdouble.htm)

[AdsGetLongLong](ace_adsgetlonglong.htm)