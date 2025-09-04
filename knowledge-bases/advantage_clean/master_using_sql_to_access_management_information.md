---
title: Master Using Sql To Access Management Information
slug: master_using_sql_to_access_management_information
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_using_sql_to_access_management_information.htm
source: Advantage CHM
tags:
  - master
checksum: 1fe17bcad6356a5842f88bbfaac22c0cbfdcfdf9
---

# Master Using Sql To Access Management Information

Using SQL to Access Management Information

Using SQL to Access Management Information

Advantage SQL Engine

| Using SQL to Access Management Information  Advantage SQL Engine |  |  |  |  |

All system procedures that have names prefixed with "sp\_mg" can be used to access Advantage Database Server management information. They provide an alternative mechanism to retrieve the same information that the Advantage Management API provides (see the Advantage Client Engine API help file). These procedures provide a way for SQL-only clients to be able to retrieve management information. Because these procedures return information through static SQL cursors, there is more cost involved than if the equivalent API function is called. The management system procedures can be called from both free connections and data dictionary connections. Other system procedures are available to return information about the currently active queries running on the server.

[sp\_CancelQuery](master_sp_cancelquery.md)

[sp\_DisableQueryLogging](master_sp_disablequerylogging.md)

[sp\_EnableQueryLogging](master_sp_enablequerylogging.md)

[sp\_GetColumns](master_sp_getcolumns.md)

[sp\_getCollations](master_sp_getcollations.htm "sp_getCollations")

[sp\_GetLinks](master_sp_getlinks.md)

[sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.md)

[sp\_GetTables](master_sp_gettables.md)

[sp\_GetSQLStatements](master_sp_getsqlstatements.md)

[sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.md)

[sp\_mgGetAllIndexes](master_sp_mggetallindexes.md)

[sp\_mgGetAllLocks](master_sp_mggetalllocks.md)

[sp\_mgGetAllTables](master_sp_mggetalltables.md)

[sp\_mgGetCommStats](master_sp_mggetcommstats.md)

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.md)

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.md)

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.md)

[sp\_mgGetCrashDumpInfo](master_sp_mggetcrashdumpinfo.md)

[sp\_mgGetIndexUsers](master_sp_mggetindexusers.md)

[sp\_mgGetInstallInfo](master_sp_mggetinstallinfo.md)

[sp\_mgGetLockOwner](master_sp_mggetlockowner.md)

[sp\_mgGetServerType](master_sp_mggetservertype.md)

[sp\_mgGetTableIndexes](master_sp_mggettableindexes.md)

[sp\_mgGetTableUsers](master_sp_mggettableusers.md)

[sp\_mgGetUsageInfo](master_sp_mggetusageinfo.md)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.md)

[sp\_mgGetUserLocks](master_sp_mggetuserlocks.md)

[sp\_mgGetUserTables](master_sp_mggetusertables.md)

[sp\_mgGetWorkerThreadActivity](master_sp_mggetworkerthreadactivity.md)

[sp\_mgKillUser](master_sp_mgkilluser.md)

[sp\_mgResetCommStats](master_sp_mgresetcommstats.md)

[sp\_mgSetConfigValue](master_sp_mgsetconfigvalue.md)

[sp\_ViewQueryLogging](master_sp_viewquerylogging.md)
