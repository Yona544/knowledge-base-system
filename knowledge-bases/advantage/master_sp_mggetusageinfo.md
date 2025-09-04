sp\_mgGetUsageInfo




Advantage Database Server 12  

sp\_mgGetUsageInfo

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetUsageInfo  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetUsageInfo Advantage SQL Engine master\_Sp\_mggetusageinfo Advantage SQL > System Procedures > Procedures > sp\_mgGetUsageInfo / Dear Support Staff, |  |
| sp\_mgGetUsageInfo  Advantage SQL Engine |  |  |  |  |

Returns information about the current activity on the Advantage Database Server.

Syntax

EXECUTE PROCEDURE sp\_mgGetUsageInfo()

Parameters

|  |  |
| --- | --- |
| Item (O) | Name of the activity. |
| InUse (O) | Number of items in use. |
| MaxUsed (O) | Maximum number of items ever used. |
| Configured (O) | Number configured on the server. |
| Rejected (O) | Number of items rejected. |

Remarks

This procedure returns the following items:

Users

Connections

Work Areas

Tables

Indexes

Locks

TPS Header Elems

TPS Visibility Elems

TPS Memo Elems

Worker Threads

Stateful Users

Stateless Users

To get the server up-time, errors logged, or number of operations use the sp\_mgGetActivityInfo procedure.

Note With the Advantage Local Server, sp\_mgGetUsageInfo will only return information for the instance of Advantage Local Server currently loaded into memory.

Example

EXECUTE PROCEDURE sp\_mgGetusageInfo();

See Also

[sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.htm)

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.htm)

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.htm)

[sp\_mgGetInstallInfo](master_sp_mggetinstallinfo.htm)