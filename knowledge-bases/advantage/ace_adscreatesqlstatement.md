AdsCreateSQLStatement




Advantage Database Server 12  

AdsCreateSQLStatement

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCreateSQLStatement  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCreateSQLStatement Advantage Client Engine ace\_Adscreatesqlstatement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCreateSQLStatement  Advantage Client Engine |  |  |  |  |

Creates an SQL statement object and returns the handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCreateSQLStatement( ADSHANDLE hConnect,  ADSHANDLE \*phStatement ) |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle |
| phStatement (O) | Statement handle returned |

Remarks

AdsCreateSQLStatement takes as input a non-zero connection handle value and returns a statement handle for use in subsequent calls to [AdsPrepareSQL](ace_adspreparesql.htm), [AdsExecuteSQL](ace_adsexecutesql.htm) , and [AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm) . After a call to AdsPrepareSQL with an SQL statement that contains parameters this statement handle can then be used in calls to the following AdsSet functions to set parameter data:

|  |  |
| --- | --- |
| · | [AdsSetBinary](ace_adssetbinary.htm) |

|  |  |
| --- | --- |
| · | [AdsSetDate](ace_adssetdate.htm) |

|  |  |
| --- | --- |
| · | [AdsSetDouble](ace_adssetdouble.htm) |

|  |  |
| --- | --- |
| · | [AdsSetJulian](ace_adssetjulian.htm) |

|  |  |
| --- | --- |
| · | [AdsSetLogical](ace_adssetlogical.htm) |

|  |  |
| --- | --- |
| · | [AdsSetLong](ace_adssetlong.htm) |

|  |  |
| --- | --- |
| · | [AdsSetMilliseconds](ace_adssetmilliseconds.htm) |

|  |  |
| --- | --- |
| · | [AdsSetShort](ace_adssetshort.htm) |

|  |  |
| --- | --- |
| · | [AdsSetString](ace_adssetstring.htm) |

|  |  |
| --- | --- |
| · | [AdsSetTime](ace_adssettime.htm) |

|  |  |
| --- | --- |
| · | [AdsSetTimeStamp](ace_adssettimestamp.htm) |

The statement handle must be closed with the [AdsCloseSQLStatement](ace_adsclosesqlstatement.htm) or [AdsApplicationExit](ace_adsapplicationexit.htm) function call.

Note When using the Advantage Database Server (ADS) SQL statements are sent to the server for processing. Because of this functionality, joins across servers are not possible when using the Advantage Database Server. Joins across servers when using Advantage Local Server, however, are legal.

Example

AdsConnect( "x:\mydata\", &hConnection );

AdsCreateSQLStatement( hConnection, &hStmt );

// EXECUTE STATEMENT, PROCESS DATA, ETC

AdsCloseSQLStatement( hStmt );

[Additional Example](ace_more_examples.htm#adscreatesqlstatementexample)

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsPrepareSQL](ace_adspreparesql.htm)

[AdsExecuteSQL](ace_adsexecutesql.htm)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm)

[AdsCloseSQLStatement](ace_adsclosesqlstatement.htm)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.htm)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.htm)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.htm)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.htm)

[AdsStmtSetTableType](ace_adsstmtsettabletype.htm)