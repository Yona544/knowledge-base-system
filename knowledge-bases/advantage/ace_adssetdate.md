AdsSetDate




Advantage Database Server 12  

AdsSetDate

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetDate  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetDate Advantage Client Engine ace\_Adssetdate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetDate  Advantage Client Engine |  |  |  |  |

Stores given date in the given date field or the date portion of a timestamp field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetDate (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  UNSIGNED8 \*pucValue,  UNSIGNED16 usLen); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| pucValue (I) | Date value as a string. |
| usLen (I) | Length of data. |

Remarks

AdsSetDate can be used to set values for date, short date, ModTime, and the date portion of timestamp fields. The date given must be in the form of the current date format as specified in a call to [AdsSetDateFormat](ace_adssetdateformat.htm). The Advantage Client Engine recognizes leap years.

If the date format includes only two digits for the year, the epoch setting is used to determine the century digits. If the year is greater than or equal to the last two digits of the epoch setting, the date is set in the epochs century. If the year is less than the last two digits of the epoch setting, the date is set in the century after the epoch setting. For example, if the epoch is 1950, a date of 10/14/53 will be set as 1953, and a date of 1/21/45 will be resolved to 2045.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.htm) and [AdsBuildRawKey](ace_adsbuildrawkey.htm).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

If using AdsSetDate to set parameters in an SQL statement the date format CCYY-MM-DD can always be used. Alternatively, the current Advantage Client Engine date format (see [AdsSetDateFormat](ace_adssetdateformat.htm)) can be used to specify the date value.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE dob > :DateOfBirth" );

AdsSetDate( hStatement, "DateOfBirth", "1976-08-24", strlen( "1976-08-24" ) );

AdsExecuteSQL( hStatement, &hCursor);

 

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE dob > :DateOfBirth" );

AdsSetDate( hStatement, ADSFIELD(1), "1976-08-24", strlen( "1976-08-24" ) );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_examples.htm#adssetdateexample)

See Also

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsSetTime](ace_adssettime.htm)

[AdsGetDate](ace_adsgetdate.htm)

[AdsSetEpoch](ace_adssetepoch.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)