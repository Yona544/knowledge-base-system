AdsSetLong




Advantage Database Server 12  

AdsSetLong

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetLong  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetLong Advantage Client Engine ace\_Adssetlong Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetLong  Advantage Client Engine |  |  |  |  |

Stores the given signed long integer in the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetLong (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  SIGNED32 lValue); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| lValue (I) | Long value to be stored in table. |

Remarks

AdsSetLong can be used to set values for numeric, long integer, integer, short integer, double, RowVersion, and CurDouble, and Money fields. If there are decimals in a numeric field, the decimals are padded with character zeros. If the number of lValue is too large to fit in the fields, ADS\_DATA\_TOO\_LONG is returned.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to AdsInitRawKey and AdsBuildRawKey.

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE count < :CountParam" );

AdsSetLong( hStatement, "CountParam", 68 );

AdsExecuteSQL( hStatement, &hCursor);

 

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE count < :CountParam" );

AdsSetLong( hStatement, ADSFIELD(1), 68 );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_examples.htm#adssetlongexample)

See Also

[AdsGetLong](ace_adsgetlong.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)

[AdsSetLongLong](ace_adssetlonglong.htm)