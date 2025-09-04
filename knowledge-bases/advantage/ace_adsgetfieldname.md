AdsGetFieldName




Advantage Database Server 12  

AdsGetFieldName

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetFieldName  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetFieldName Advantage Client Engine ace\_Adsgetfieldname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetFieldName  Advantage Client Engine |  |  |  |  |

Retrieves the name of a field in a table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetFieldName (ADSSHANDLE hTable,  UNSIGNED16 usFld,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusBufLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| usFld (I) | Field position of interest (the first field is 1). |
| pucName (O) | Returns the name of the field. |
| pusBufLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

Retrieves the name of a field in a table. For ADT tables, valid field names are 128 characters or less and can contain any character value except 0 (NULL), ";" (a semi-colon), or "," (a comma). For DBF tables, valid field names are 10 characters or less. Valid characters for field names are the letters a-z and A-Z, digits 0-9, and the underscore "\_" character.

When using SQL statements the table handle parameter can be replaced with a cursor handle. In this situation AdsGetFieldName will return the name of the specified column in the rowset.

Note If retrieving a column name from a rowset that contains alias columns these aliases are respected. For example, after executing "SELECT lname LastName FROM test" a call to AdsGetFieldName with column 1 would return "LastName".

Example

[Click Here](ace_examples.htm#adsgetfieldnameexample)

See Also

[AdsGetFieldNum](ace_adsgetfieldnum.htm)

[AdsGetNumFields](ace_adsgetnumfields.htm)