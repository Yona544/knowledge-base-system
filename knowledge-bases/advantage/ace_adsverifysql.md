AdsVerifySQL




Advantage Database Server 12  

AdsVerifySQL / AdsVerifySQLW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsVerifySQL / AdsVerifySQLW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsVerifySQL / AdsVerifySQLW Advantage Client Engine ace\_Adsverifysql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsVerifySQL / AdsVerifySQLW  Advantage Client Engine |  |  |  |  |

Verifies the validity of an SQL statement without executing it

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsVerifySQL( ADSHANDLE hStatement,               UNSIGNED8 \*pucSQL ) |
| UNSIGNED32 | AdsVerifySQLW( ADSHANDLE hStatement,                WCHAR     \*pwcSQL ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |
| pucSQL (I) | The SQL statement given as an ANSI encoded null terminated string. |
| pwcSQL (I) | The SQL statement given as a UTF-16 encoded null terminated Unicode string. UTF-16LE encoding is assumed unless the first two characters are the BOM indicating the encoding is UTF-16BE. |

Remarks

AdsVerifySQL and AdsVerifySQLW are useful to call prior to executing a time consuming SQL statement or to test a dynamically created SQL statement. The only difference between the two functions is the encoding of the SQL statement.

Example

ulRetVal = AdsVerifySQL( hStatement, "SELECT \* FROM demo10");

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "Invalid SQL statement" );

return ulRetVal;

}

ulRetVal = AdsExecute( hSQL, &hCursor );

 

See Also

[AdsPrepareSQL](ace_adspreparesql.htm)

[AdsPrepareSQLW](ace_adspreparesql.htm)

[AdsExecuteSQL](ace_adsexecutesql.htm)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm)