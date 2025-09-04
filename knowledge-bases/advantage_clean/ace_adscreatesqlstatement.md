---
title: Ace Adscreatesqlstatement
slug: ace_adscreatesqlstatement
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscreatesqlstatement.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8af476818bc1f22f892c3c4b3b49299dda4fba07
---

# Ace Adscreatesqlstatement

AdsCreateSQLStatement

AdsCreateSQLStatement

Advantage Client Engine

| AdsCreateSQLStatement  Advantage Client Engine |  |  |  |  |

Creates an SQL statement object and returns the handle

Syntax

| UNSIGNED32 | AdsCreateSQLStatement( ADSHANDLE hConnect,  ADSHANDLE \*phStatement ) |

Parameters

| hConnect (I) | Connection handle |
| phStatement (O) | Statement handle returned |

Remarks

AdsCreateSQLStatement takes as input a non-zero connection handle value and returns a statement handle for use in subsequent calls to [AdsPrepareSQL](ace_adspreparesql.md), [AdsExecuteSQL](ace_adsexecutesql.md) , and [AdsExecuteSQLDirect](ace_adsexecutesqldirect.md) . After a call to AdsPrepareSQL with an SQL statement that contains parameters this statement handle can then be used in calls to the following AdsSet functions to set parameter data:

- [AdsSetBinary](ace_adssetbinary.md)

- [AdsSetDate](ace_adssetdate.md)

- [AdsSetDouble](ace_adssetdouble.md)

- [AdsSetJulian](ace_adssetjulian.md)

- [AdsSetLogical](ace_adssetlogical.md)

- [AdsSetLong](ace_adssetlong.md)

- [AdsSetMilliseconds](ace_adssetmilliseconds.md)

- [AdsSetShort](ace_adssetshort.md)

- [AdsSetString](ace_adssetstring.md)

- [AdsSetTime](ace_adssettime.md)

- [AdsSetTimeStamp](ace_adssettimestamp.md)

The statement handle must be closed with the [AdsCloseSQLStatement](ace_adsclosesqlstatement.md) or [AdsApplicationExit](ace_adsapplicationexit.md) function call.

Note When using the Advantage Database Server (ADS) SQL statements are sent to the server for processing. Because of this functionality, joins across servers are not possible when using the Advantage Database Server. Joins across servers when using Advantage Local Server, however, are legal.

Example

AdsConnect( "x:\mydata\", &hConnection );

AdsCreateSQLStatement( hConnection, &hStmt );

// EXECUTE STATEMENT, PROCESS DATA, ETC

AdsCloseSQLStatement( hStmt );

[Additional Example](ace_more_examples.md#adscreatesqlstatementexample)

See Also

[AdsConnect](ace_adsconnect.md)

[AdsPrepareSQL](ace_adspreparesql.md)

[AdsExecuteSQL](ace_adsexecutesql.md)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.md)

[AdsCloseSQLStatement](ace_adsclosesqlstatement.md)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.md)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.md)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.md)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.md)

[AdsStmtSetTableType](ace_adsstmtsettabletype.md)
