sp\_mgGetConfigMemory




Advantage Database Server 12  

sp\_mgGetConfigMemory

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetConfigMemory  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetConfigMemory Advantage SQL Engine master\_Sp\_mggetconfigmemory Advantage SQL > System Procedures > Procedures > sp\_mgGetConfigMemory / Dear Support Staff, |  |
| sp\_mgGetConfigMemory  Advantage SQL Engine |  |  |  |  |

Returns Advantage Database Server configuration information that affects the amount of memory required by the Advantage Database Server

Syntax

EXECUTE PROCEDURE sp\_mgGetConfigMemory()

Parameters

|  |  |
| --- | --- |
| Item (O) | Name of the item. |
| Value (O) | Value from the server. |
| Memory (O) | Amount of memory used in bytes. |

Remarks

This procedure returns the following items:

Connections

Work Areas

Tables

Indexes

Locks

User Buffer Size

TPS Header Elems

TPS Visibility Elems

TPS Memo Elems

Receive ECBs

Send ECBs

Worker Threads

Total Memory

Example

EXECUTE PROCEDURE sp\_mgGetConfigMemory();

See Also

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.htm)