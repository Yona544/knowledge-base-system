AdsExecuteSQLDirect




Advantage Database Server 12  

AdsExecuteSQLDirect / AdsExecuteSQLDirectW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExecuteSQLDirect / AdsExecuteSQLDirectW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsExecuteSQLDirect / AdsExecuteSQLDirectW Advantage Client Engine ace\_Adsexecutesqldirect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsExecuteSQLDirect / AdsExecuteSQLDirectW  Advantage Client Engine |  |  |  |  |

Executes an SQL statement

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsExecuteSQLDirect( ADSHANDLE hStatement,                      UNSIGNED8 \*pucSQL,                      ADSHANDLE \*phCursor ) |
| UNSIGNED32 | AdsExecuteSQLDirect( ADSHANDLE hStatement,                      WCHAR     \*pwcSQL,                      ADSHANDLE \*phCursor ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm) . |
| pucSQL (I) | The SQL statement given as an ANSI code page encoded null terminated string. |
| pwcSQL (I) | The SQL statement given as a UTF-16 encoded null terminated Unicode string. UTF-16LE encoding is assumed unless the first two characters are the BOM indicating the encoding is UTF-16BE. |
| phCursor (O) | Returns the cursor handle if executing a SELECT statement, otherwise returns NULL. |

Remarks

AdsExecuteSQLDirect and AdsExecuteSQLDirect100 are a combination of [AdsPrepareSQL](ace_adspreparesql.htm) and [AdsExecuteSQL](ace_adsexecutesql.htm). The SQL statement cannot have parameters. If parameters are required, use AdsPrepareSQL or AdsPrepareSQLW and AdsExecuteSQL. The only difference between the two functions is the encoding of the SQL statement.

The value returned in the phCursor parameter is dependent on the type of SQL statement being executed. If executing a SELECT statement a handle to the cursor will be returned, and this cursor handle can then be used in calls that accept normal ADS table handles (e.g., [AdsGetField](ace_adsgetfield.htm)). If executing a statement other than a SELECT the phCursor parameter can be passed in as NULL. If executing a statement other than a SELECT and the phCursor parameter is not passed in as NULL, it will be set to NULL by AdsExecuteSQLDirect.

If the SQL statement is an UPDATE statement the statement handle can be passed to [AdsGetRecordCount](ace_adsgetrecordcount.htm) to determine how many rows were affected by the UPDATE statement.

If the statement handle has an open cursor associated with it AdsExecuteSQLDirect will return an error. The cursor must first be closed with [AdsCloseTable](ace_adsclosetable.htm).

After the SQL statement has been executed a cursor handle will be returned. This cursor handle provides access to the rowset returned. Note that statements other than SELECT statements will not return a rowset, therefore they will not return a cursor (e.g., INSERT, UPDATE). Except for the APIs listed below this cursor handle can take the place of a table handle in any Advantage Client Engine API. For example, API AdsGetField is documented as accepting a table handle for its first parameter. This table handle can be replaced with a cursor handle to obtain data from the rowset:

 AdsGetField( hCursor, "lastname", aucBuffer,

&ulLen, ADS\_TRIM );

The following APIs are not compatible with cursor handles:

|  |  |
| --- | --- |
| · | •   AdsDecryptTable |

|  |  |
| --- | --- |
| · | •   AdsEncryptTable |

|  |  |
| --- | --- |
| · | •   AdsPackTable |

|  |  |
| --- | --- |
| · | •   AdsZapTable |

|  |  |
| --- | --- |
| · | •   AdsReindex |

Cursors returned by SELECT statements may be static cursors or dynamic cursors (updateable). See the family of AdsStmtSet APIs for information on specifying a cursor as read-only or updateable. [AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm) can be used to determine if the returned cursor is read-only (and thus static) or not.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_more_examples.htm#adsexecutesqldirectexample)

See Also

[AdsPrepareSQL](ace_adspreparesql.htm)

[AdsPrepareSQLW](ace_adspreparesql.htm)

[AdsExecuteSQL](ace_adsexecutesql.htm)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.htm)

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsVerifySQL](ace_adsverifysql.htm)

[AdsVerifySQLW](ace_adsverifysql.htm)