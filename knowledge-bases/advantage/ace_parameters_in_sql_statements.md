Parameters in SQL Statements




Advantage Database Server 12  

Parameters in SQL Statements

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parameters in SQL Statements  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Parameters in SQL Statements Advantage Client Engine ace\_Parameters\_in\_sql\_statements Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Parameters in SQL Statements  Advantage Client Engine |  |  |  |  |

It is not possible to utilize the AdsExecuteSQLDirect API when the statement to be executed contains parameters. This situation requires the use of AdsPrepareSQL and AdsExecuteSQL.

The Advantage Client Engine supports named parameters as well as unnamed parameters. An unnamed parameter is represented with a question mark (?). Named parameters are represented with a string preceded by a colon. The "String" portion may contain the characters 0..9, A..Z, a..z, or the underscore character (\_). Any sub-string in the SQL statement that meets the following criteria will be assumed to be a named parameter:

|  |  |
| --- | --- |
| · | The sub-string is of the form ":String" |

|  |  |
| --- | --- |
| · | The sub-string is not within a quoted string |

NAMED PARAMETER EXAMPLE - "select \* from test where lastname = :value"

UNNAMED PARAMETER EXAMPLE - "select \* from test where lastname = ?"

Once the call to AdsPrepareSQL has been performed, the AdsSet\* functions (e.g., AdsSetString, AdsSetDate, AdsSetDouble, etc.) may be used to assign values to parameters.

Each of the AdsSet\* functions has at least three parameters: hAdsHandle, pucFieldName, and xxxValue. When filling in SQL parameters, pass the statement handle that has been prepared as the hAdsHandle value. Then use pucFieldName to indicate the parameter name or number and xxxValue to set the parameters value.

Example 1

AdsPrepareSQL( hStatement, "select \* from test where lastname < :name" );

AdsSetString( hStatement, "name", "Anderson", strlen("Anderson") );

AdsExecuteSQL( hStatement, &hCursor);

The pucFieldName argument can reference a string that stores the named parameter name or it can contain a parameter number. Every parameter may be referenced by a number regardless if it is named or unnamed. The numbers start with 1 (one) and increment from left to right.

Example 2

AdsPrepareSQL( hStatement, "select \* from test where lastname < :name" );

AdsSetString( hStatement, ADSFIELD(1), "Anderson", strlen("Anderson") );

AdsExecuteSQL( hStatement, &hCursor);

Subsequent calls to AdsExecuteSQL will cause only changed parameter values or SQL statements to be sent to the server. Thus, using prepared statements can be more efficient than direct execution if a statement is going to be executed multiple times.

Example 3

AdsPrepareSQL( hStatement, "select \* from test where lastname = :lname and firstname = : fname" );

AdsSetString( hStatement, "lname", "Anderson", strlen("Anderson") );

AdsSetString( hStatement, "fname", "John", strlen("John") );

AdsExecuteSQL( hStatement, &hCursor);

// now close the cursor and change one of the parameters

AdsCloseTable( hCursor );

AdsSetString( hStatement, "fname", "Frank", strlen("Frank") );

// now the statement will resolve to

// "select \* from test where lastname = Anderson and firstname = Frank " );

AdsExecuteSQL( hStatement, &hCursor );

If the SQL statement is changed, the old parameter values will be matched with the new statement by using the parameter position (relative to other parameters). Use AdsClearSQLParams to destroy all parameters and free their associated memory. A call to AdsCloseSQLStatement will also free all parameters.