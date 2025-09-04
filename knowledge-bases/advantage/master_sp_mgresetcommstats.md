sp\_mgResetCommStats




Advantage Database Server 12  

sp\_mgResetCommStats

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgResetCommStats  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgResetCommStats Advantage SQL Engine master\_Sp\_mgresetcommstats Advantage SQL > System Procedures > Procedures > sp\_mgResetCommStats / Dear Support Staff, |  |
| sp\_mgResetCommStats  Advantage SQL Engine |  |  |  |  |

Resets all Advantage Database Server communication statistics to zero.

Syntax

EXECUTE PROCEDURE sp\_mgResetCommStats()

Parameters

NONE

Remarks

This procedure resets all Advantage Database Server communication statistics to zero. This Advantage Management Procedure is useful when used in conjunction with sp\_mgGetCommStats to determine how often corrupted packets are being discovered.

Example

EXECUTE PROCEDURE sp\_mgResetCommStats();

See Also

[sp\_mgGetCommStats](master_sp_mggetcommstats.htm)