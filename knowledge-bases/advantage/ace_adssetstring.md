AdsSetString




Advantage Database Server 12  

AdsSetString / AdsSetStringW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetString / AdsSetStringW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetString / AdsSetStringW Advantage Client Engine ace\_Adssetstring Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetString / AdsSetStringW  Advantage Client Engine |  |  |  |  |

Sets a field value in a table to a string value.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetString ( ADSHANDLE hObj,                UNSIGNED8 \*pucFldName,                UNSIGNED8 \*pucBuf,                UNSIGNED32 ulLen ); |
| UNSIGNED32 | AdsSetStringW( ADSHANDLE hObj,                UNSIGNED8  \*pucFldName,                WCHAR      \*pwcBuf,                UNSIGNED32 ulLen ); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| pucBuf (I) | Store this ANSI/OEM code page encoded string data in the field. |
| pwcBuf (I) | Store this UTF16 encoded Unicode string in the field. |
| ulLen (I) | Length of data in the buffer. For AdsSetString, the length is  the number of bytes. For AdsSetStringW, the length is the number of UTF16 characters. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_DATA\_TRUNCATED | The data given was too long to fit in the field. The data was truncated to fit. |
| AE\_UNICODE\_CONVERSION | The Unicode data given cannot be converted into ANSI/OEM code page encoded string to stored in a non-Unicode field. |

Remarks

AdsSetString and AdsSetStringW can be used to set values for character, memo, and logical fields. To set numeric and date fields with string values, use [AdsSetField](ace_adssetfield.htm). Be sure to be precise with the ulLen parameter, or unwanted data could be copied into a field.  Binary data that is encoded as a base64 string can set using this API.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to AdsInitRawKey and AdsBuildRawKey.

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.htm). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the ordinal number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE lastname = :lname AND firstname = : fname" );

AdsSetString( hStatement, "lname", "Anderson", strlen("Anderson") );

AdsSetString( hStatement, ADSFIELD(2), "John", strlen("John") );

AdsExecuteSQL( hStatement, &hCursor);

 

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE lastname = :lname AND firstname = : fname" );

AdsSetString( hStatement, ADSFIELD(1), "Anderson",

strlen("Anderson") );

AdsSetString( hStatement, ADSFIELD(2), "John", strlen("John") );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_examples.htm#adssetstringexample)

See Also

[AdsGetString](ace_adsgetstring.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsSetFieldW](ace_adssetfield.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)

[AdsPrepareSQLW](ace_adspreparesql.htm)