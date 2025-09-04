AdsPrepareSQL




Advantage Database Server 12  

AdsPrepareSQL / AdsPrepareSQLW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsPrepareSQL / AdsPrepareSQLW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsPrepareSQL / AdsPrepareSQLW Advantage Client Engine ace\_Adspreparesql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsPrepareSQL / AdsPrepareSQLW  Advantage Client Engine |  |  |  |  |

Prepares an SQL statement for execution

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsPrepareSQL( ADSHANDLE hStatement,                UNSIGNED8 \*pucSQL ) |
| UNSIGNED32 | AdsPrepareSQLW( ADSHANDLE hStatement,                 WCHAR \*pwcSQL ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |
| pucSQL (I) | The SQL statement given as an ANSI code page encoded null terminated string. |
| pwcSQL (I) | The SQL statement given as a UTF-16 encoded null terminated Unicode string. UTF-16LE encoding is assumed unless the first two characters are the BOM indicating the encoding is UTF-16BE. |

Remarks

Use AdsPrepareSQL or AdsPrepareSQLW when executing SQL statements that contain parameters. The only difference between the two functions is the encoding of the SQL statement.

The Advantage Client Engine supports named parameters as well as unnamed parameters. An unnamed parameter is represented with a question mark (?). Named parameters are represented with a string preceded by a colon. The "String" portion may contain the characters 0..9, A..Z, a..z, or the underscore character (\_). Any sub-string in the SQL statement that meets the following criteria will be assumed to be a named parameter:

|  |  |
| --- | --- |
| · | It is of the form ":String" |

|  |  |
| --- | --- |
| · | It is not within a quoted string |

|  |  |
| --- | --- |
| NAMED PARAMETER EXAMPLE | "select \* from test where lastname = :value" |
| UNNAMED PARAMETER EXAMPLE | "select \* from test where lastname = ?" |

Once the call to AdsPrepareSQL has been performed the AdsSet family of functions may be used to assign values to parameters.

Each of the AdsSet\* functions has at least three parameters: hAdsHandle, pucFieldName, and xxxValue. When defining SQL parameters, pass the statement handle that has been prepared as the hAdsHandle value. Then use pucFieldName to indicate the parameter name/number and xxxValue to set the parameters value.

Example 1

AdsPrepareSQL( hStatement, "select \* from test where lastname < :name" );

AdsSetString( hStatement, "name", "Anderson", strlen("Anderson") );

AdsExecuteSQL( hStatement, &hCursor);

The pucFieldName argument can reference a string that stores the named parameter name or it can contain a parameter number. Every parameter may be referenced by a number regardless if it is named or unnamed. The numbers start with 1 and increment from left to right.

Example 2

AdsPrepareSQL( hStatement, "select \* from test where lastname < :name" );

AdsSetString( hStatement, ADSFIELD(1), "Anderson", strlen("Anderson") );

AdsExecuteSQL( hStatement, &hCursor);

Subsequent calls to AdsExecuteSQL will cause only changed parameter values or SQL statements to be sent to the server.

Example 3

AdsPrepareSQL( hStatement,

"select \* from test where lastname = :lname and firstname = : fname" );

AdsSetString( hStatement, "lname", "Anderson", strlen("Anderson") );

AdsSetString( hStatement, "fname", "John", strlen("John") );

AdsExecuteSQL( hStatement, &hCursor);

// now close the cursor and change one of the parameters

AdsCloseTable( hCursor );

AdsSetString( hStatement, "fname", "Frank", strlen("Frank") );

// now the statement will resolve to

// "select \* from test where lastname = Anderson and firstname = Frank " );

AdsExecuteSQL( hStatement, &hCursor );

If the SQL statement is changed, the old parameter values will be matched with the new statement by using the parameter number. Use AdsClearSQLParams to destroy all parameters and free their associated memory.

If the statement handle has an open cursor associated with it, AdsPrepareSQL will return an error. The cursor must first be closed with AdsCloseTable.

Example

[Additional Example](ace_more_examples.htm#adspreparesqlexample)

See Also

[AdsExecuteSQL](ace_adsexecutesql.htm)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm)

[AdsExecuteSQLDirectW](ace_adsexecutesqldirect.htm)

[AdsClearSQLParams](ace_adsclearsqlparams.htm)

[AdsCloseTable](ace_adsclosetable.htm)

[AdsVerifySQL](ace_adsverifysql.htm)

[AdsVerifySQLW](ace_adsverifysql.htm)