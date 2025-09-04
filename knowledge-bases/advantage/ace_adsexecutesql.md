AdsExecuteSQL




Advantage Database Server 12  

AdsExecuteSQL

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExecuteSQL  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsExecuteSQL Advantage Client Engine ace\_Adsexecutesql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsExecuteSQL  Advantage Client Engine |  |  |  |  |

Executes a prepared SQL statement

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsExecuteSQL( ADSHANDLE hStatement,  ADSHANDLE \*phCursor ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement that has been used in a previous call to AdsPrepareSQL. |
| phCursor (O) | Returns the cursor handle if executing a SELECT statement, otherwise returns NULL. |

Remarks

AdsExecuteSQL executes a statement that has been prepared by a previous call to [AdsPrepareSQL](ace_adspreparesql.htm). Use of this API is required when executing an SQL statement that contains parameters. If executing a statement that does not contain parameters, it is simpler to call [AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm), which does not require a call to AdsPrepareSQL.

The value returned in the phCursor parameter is dependent on the type of SQL statement being executed. If executing a SELECT statement a handle to the cursor will be returned, and this cursor handle can then be used in calls that accept normal ADS table handles (e.g., [AdsGetField](ace_adsgetfield.htm)). If executing a statement other than a SELECT the phCursor parameter can be passed in as NULL. If executing a statement other than a SELECT and the phCursor parameter is not passed in as NULL, it will be set to NULL by AdsExecuteSQL.

If the SQL statement is an UPDATE statement the statement handle can be passed to [AdsGetRecordCount](ace_adsgetrecordcount.htm) to determine how many rows were affected by the UPDATE statement. If this value is desired it must be retrieved prior to the next call to AdsPrepareSQL.

If the statement handle has an open cursor associated with it AdsExecuteSQL will return an error. The cursor must first be closed with [AdsCloseTable](ace_adsclosetable.htm).

After the SQL statement has been executed a cursor handle will be returned. This cursor handle provides access to the rowset returned. Note that statements other than SELECT statements will not return a rowset, therefore they will not return a cursor (e.g., INSERT, UPDATE). Except for the APIs listed below this cursor handle can take the place of a table handle in any Advantage Client Engine API. For example, AdsGetField is documented as accepting a table handle for its first parameter. This table handle can be replaced with a cursor handle to obtain data from the rowset:

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
| · | •   AdsDecryptRecord |

|  |  |
| --- | --- |
| · | •   AdsEncryptRecord |

|  |  |
| --- | --- |
| · | •   AdsPackTable |

|  |  |
| --- | --- |
| · | •   AdsZapTable |

|  |  |
| --- | --- |
| · | •   AdsReindex |

|  |  |
| --- | --- |
| · | •   AdsLockTable |

|  |  |
| --- | --- |
| · | •   AdsUnlockTable |

Cursors returned by SELECT statements may be static cursors or dynamic cursors (updateable). See the family of AdsStmtSet APIs for information on specifying a cursor as read-only or updateable. [AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm) can be used to determine if the returned cursor is read-only (and thus static) or not.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_more_examples.htm#adsexecutesqlexample)

See Also

[AdsPrepareSQL](ace_adspreparesql.htm)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.htm)

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsClearSQLParams](ace_adsclearsqlparams.htm)

[AdsVerifySQL](ace_adsverifysql.htm)