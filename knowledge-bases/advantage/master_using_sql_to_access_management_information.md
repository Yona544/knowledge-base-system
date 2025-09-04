Using SQL to Access Management Information




Advantage Database Server 12  

Using SQL to Access Management Information

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using SQL to Access Management Information  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using SQL to Access Management Information Advantage SQL Engine master\_Using\_sql\_to\_access\_management\_information Advantage SQL > System Procedures > Using SQL to Access Management Information / Dear Support Staff, |  |
| Using SQL to Access Management Information  Advantage SQL Engine |  |  |  |  |

All system procedures that have names prefixed with "sp\_mg" can be used to access Advantage Database Server management information. They provide an alternative mechanism to retrieve the same information that the Advantage Management API provides (see the Advantage Client Engine API help file). These procedures provide a way for SQL-only clients to be able to retrieve management information. Because these procedures return information through static SQL cursors, there is more cost involved than if the equivalent API function is called. The management system procedures can be called from both free connections and data dictionary connections. Other system procedures are available to return information about the currently active queries running on the server.

[sp\_CancelQuery](master_sp_cancelquery.htm)

[sp\_DisableQueryLogging](master_sp_disablequerylogging.htm)

[sp\_EnableQueryLogging](master_sp_enablequerylogging.htm)

[sp\_GetColumns](master_sp_getcolumns.htm)

[sp\_getCollations](master_sp_getcollations.htm "sp_getCollations")

[sp\_GetLinks](master_sp_getlinks.htm)

[sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.htm)

[sp\_GetTables](master_sp_gettables.htm)

[sp\_GetSQLStatements](master_sp_getsqlstatements.htm)

[sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.htm)

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.htm)

[sp\_mgGetAllLocks](master_sp_mggetalllocks.htm)

[sp\_mgGetAllTables](master_sp_mggetalltables.htm)

[sp\_mgGetCommStats](master_sp_mggetcommstats.htm)

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.htm)

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.htm)

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.htm)

[sp\_mgGetCrashDumpInfo](master_sp_mggetcrashdumpinfo.htm)

[sp\_mgGetIndexUsers](master_sp_mggetindexusers.htm)

[sp\_mgGetInstallInfo](master_sp_mggetinstallinfo.htm)

[sp\_mgGetLockOwner](master_sp_mggetlockowner.htm)

[sp\_mgGetServerType](master_sp_mggetservertype.htm)

[sp\_mgGetTableIndexes](master_sp_mggettableindexes.htm)

[sp\_mgGetTableUsers](master_sp_mggettableusers.htm)

[sp\_mgGetUsageInfo](master_sp_mggetusageinfo.htm)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.htm)

[sp\_mgGetUserLocks](master_sp_mggetuserlocks.htm)

[sp\_mgGetUserTables](master_sp_mggetusertables.htm)

[sp\_mgGetWorkerThreadActivity](master_sp_mggetworkerthreadactivity.htm)

[sp\_mgKillUser](master_sp_mgkilluser.htm)

[sp\_mgResetCommStats](master_sp_mgresetcommstats.htm)

[sp\_mgSetConfigValue](master_sp_mgsetconfigvalue.htm)

[sp\_ViewQueryLogging](master_sp_viewquerylogging.htm)