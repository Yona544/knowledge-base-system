sp\_mgGetCrashDumpInfo




Advantage Database Server 12  

sp\_mgGetCrashDumpInfo

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetCrashDumpInfo  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetCrashDumpInfo Advantage SQL Engine master\_sp\_mgGetCrashDumpInfo Advantage SQL > System Procedures > Procedures > sp\_mgGetCrashDumpInfo / Dear Support Staff, |  |
| sp\_mgGetCrashDumpInfo  Advantage SQL Engine |  |  |  |  |

Retrieve a listing of ADSDump files located  on the server.

Syntax

EXECUTE PROCEDURE sp\_mgGetCrashDumpInfo()

Parameters

|  |  |
| --- | --- |
| CrashDumpName (O) | Filename of the ADSDump file. |
| CreationTime (O) | Timestamp the ADSDump file was created from the OS.  Note: This may differ slightly from the timestamp in the ADSDump filename. |
| FileSize (O) | The size of the file in Bytes. |

Remarks

sp\_mgGetCrashDumpInfo is an administrative procedure that will list the names, dates, and sizes of any existing crash dump files on the system.  This procedure may only be run on the active [root dictionary](master_root_dictionary.htm) and the user must be a member of the SERVER:Admin group.

Example

EXECUTE PROCEDURE sp\_mgGetCrashDumpInfo();