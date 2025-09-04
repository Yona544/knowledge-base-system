---
title: Master Sp Enablequerylogging
slug: master_sp_enablequerylogging
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_enablequerylogging.htm
source: Advantage CHM
tags:
  - master
checksum: 357e834a398db4be64f09f01256c3cbda4c54fdd
---

# Master Sp Enablequerylogging

sp\_EnableQueryLogging

sp\_EnableQueryLogging

Advantage SQL Engine

| sp\_EnableQueryLogging  Advantage SQL Engine |  |  |  |  |

Enables debug query logging.

Syntax

sp\_EnableQueryLogging(

 TableName, Character, 255,

 TruncateExistingData, Boolean,

 LogOnlyUnoptimizedQueries, Boolean,

 MinimumTimeBeforeLogging, Integer,

 EncryptionPassword, Character, 20 )

sp\_EnableQueryLogging(

 TableName, Character, 255,

 TruncateExistingData, Boolean,

 LogOnlyUnoptimizedQueries, Boolean,

 MinimumTimeBeforeLogging, Integer,

 EncryptionPassword, Character, 20,

 Options, Integer )

Parameters

| TableName (I) | Name of the table to log queries in. |
| TruncateExistingData (I) | True if existing data should be removed from the table. |
| LogOnlyUnoptimizedQueries (I) | When True, only queries that are un-optimized are logged. |
| MinimmTimeBeforeLogging (I) | The minimum number of seconds a query must be processed by before it will be logged. A value of NULL or 0 means log all queries. |
| EncryptionPassword (I) | On free connections, the password to use if the log table is encrypted. |
| Options (I) | Bit field controlling other query logging options. The current supported options are:  0x00000001 - QL\_OPTION\_ERROR\_ONLY. Only log queries that generate error.  0x00000002 - QL\_OPTION\_NO\_ERROR. Do not log queries that generate error.  These two options are mutually exclusive. |

Remarks

sp\_EnableQueryLogging is a debug system procedure that forces the Advantage Database Server or Advantage Local Server to log all queries that are executed on the current data dictionary or all queries on non-data dictionary connections. If the server is restarted, query logging must be re-enabled. Because query logging increases the amount of work required to execute a query, it is strongly suggested that this feature only be used during development. To enable query logging on a data dictionary, the user must be logged in as the administrative user, ADSSYS.

This system stored procedure is overloaded. The additional parameter in the second form currently controls how query logging handles erroneous SQL statements. The options allows the query logging to only log queries that return error or do not log queries that return error. Note: The QL\_OPTION\_NO\_ERROR option will filter out logging of SQL statements that have syntax or semantic error. SQL statements that have runtime error, i.e. such as incorrect inputs to scalar function or out of range data, will still be logged in the query log table.

The query log table has the following structure.

| Name | Type | Size | Comments |
| ID | autoinc | 4 | Unique identifier for the query. |
| Start Time | timestamp | 8 | Time and date that the query was began. |
| Optimized | boolean | 1 | True if the query is properly optimized. |
| Return Code | integer | 4 | Return Value of the query. |
| Rows Affected | integer | 4 | Number of rows affected by the query. |
| End Time | timestamp | 8 | Time and date that the query was ended. |
| Run Time | double | 8 | Elapsed time the query was processed by the server in milliseconds. |
| Database | char | 255 | Name of the database the user is connected to. |
| User Name | char | 100 | User name for data dictionary connections. |
| Connection Name | char | 100 | Connection name. |
| Application ID | memo | variable | Application ID of the application executing the query. |
| Query | memo | variable | The query that was executed. |
| Description | memo | variable | Detail error message or other miscellaneous information. |

See Also

[sp\_DisableQueryLogging](master_sp_disablequerylogging.md)

[sp\_ViewQueryLogging](master_sp_viewquerylogging.md)

[sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.md)
