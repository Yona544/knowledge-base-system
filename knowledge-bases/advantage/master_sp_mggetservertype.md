sp\_mgGetServerType




Advantage Database Server 12  

sp\_mgGetServerType

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetServerType  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetServerType Advantage SQL Engine master\_Sp\_mggetservertype Advantage SQL > System Procedures > Procedures > sp\_mgGetServerType / Dear Support Staff, |  |
| sp\_mgGetServerType  Advantage SQL Engine |  |  |  |  |

Returns the type of server the connection is to.

Syntax

EXECUTE PROCEDURE sp\_mgGetServerType()

Parameters

|  |  |
| --- | --- |
| ServerType (O) | Type of server |
| ServerTypeValue (O) | Numeric value representing server type. This is the same value as is returned by AdsMgGetServerType. |
| OSMajor (O) | Major version of the server's operation system, if available. |
| OSMinor (O) | Minor version of the server's operating system, if available. |

Remarks

Possible return values for ServerType include the following. The corresponding numeric ServerTypeValue is included in parentheses.

Windows Server (2)

Local Server (3)

Windows 9x (4)

Linux (6)

Windows 64-bit (7)

Linux 64-bit (8)

Example

EXECUTE PROCEDURE sp\_mgGetServerType();

See Also

[sp\_mgGetInstallInfo](master_sp_mggetinstallinfo.htm)