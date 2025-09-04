AdsSetDouble




Advantage Database Server 12  

AdsSetDouble

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetDouble  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetDouble Advantage Client Engine ace\_Adssetdouble Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetDouble  Advantage Client Engine |  |  |  |  |

Stores the given floating point value (IEEE 64-bit double format) in the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetDouble (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  DOUBLE64 dValue); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| dValue (I) | Store this data in the field. |

Remarks

AdsSetDouble can be used to set values for numeric, long integer, integer, short integer, double, CurDouble, RowVersion, and Money fields. It is possible to lose decimal precision using AdsSetDouble depending on the size and number of decimals in the target field. AdsSetDouble will round decimals to the precision of the field in the table whose value is being set. If the value is too large to put in the field, the function returns AE\_DATA\_TOO\_LONG. If AdsSetDouble is used to set a Money field, the double value will be rounded to the fourth decimal.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.htm) and [AdsBuildRawKey](ace_adsbuildrawkey.htm).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE average > :AvgParam" );

AdsSetDouble( hStatement, "AvgParam", 75.49 );

AdsExecuteSQL( hStatement, &hCursor);

 

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE average > :AvgParam" );

AdsSetDouble( hStatement, ADSFIELD(1), 75.49 );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_examples.htm#adssetdoubleexample)

See Also

[AdsGetDouble](ace_adsgetdouble.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)