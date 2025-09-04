AdsSetJulian




Advantage Database Server 12  

AdsSetJulian

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetJulian  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetJulian Advantage Client Engine ace\_Adssetjulian Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetJulian  Advantage Client Engine |  |  |  |  |

Stores the given Julian date in the given field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetJulian (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  SIGNED32 lDate); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| lDate (I) | Julian representation of the date. |

Remarks

AdsGetJulian can be used store the Julian date representation of a date into date, short date, ModTime, and timestamp fields. A Julian date is a signed long integer representation of the number of days since January 1, 4713 B.C.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to AdsInitRawKey and AdsBuildRawKey.

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE dob > :DateOfBirth" );

AdsSetJulian( hStatement, "DateOfBirth", 2443014 ); // 2443014 = 08/24/1976

AdsExecuteSQL( hStatement, &hCursor);

 

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE dob > :DateOfBirth" );

AdsSetJulian( hStatement, ADSFIELD(1), 2443014 ); // 2443014 = 08/24/1976

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_examples.htm#adssetjulianexample)

See Also

[AdsGetJulian](ace_adsgetjulian.htm)

[AdsSetDate](ace_adssetdate.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)