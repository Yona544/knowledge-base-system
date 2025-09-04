sp\_mgGetInstallInfo




Advantage Database Server 12  

sp\_mgGetInstallInfo

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetInstallInfo  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetInstallInfo Advantage SQL Engine master\_Sp\_mggetinstallinfo Advantage SQL > System Procedures > Procedures > sp\_mgGetInstallInfo / Dear Support Staff, |  |
| sp\_mgGetInstallInfo  Advantage SQL Engine |  |  |  |  |

Returns Advantage Database Server Installation information.

Syntax

EXECUTE PROCEDURE sp\_mgGetInstallInfo()

Parameters

|  |  |
| --- | --- |
| Owner (O) | Registered Owner |
| SerialNumber (O) | Server serial number |
| UserOption (O) | Maximum concurrent connected users allowed |
| Version (O) | Server version number |
| InstallDate (O) | Date the server was installed |
| EvalExpireDate (O) | Date the server evaluation will expire |
| ANSI (O) | ANSI character set language |
| OEM (O) | OEM character set language |
| ReplicationEnabled (O) | Indicates if the server is licensed for replication |
| MaxStatefulUsers (O) | The maximum number of configured fully connected (stateful) users |
| MaxStatelessUsers (O) | The maximum number of configured Advantage Web Platform (stateless) users |

Remarks

This procedure uses the AdsMgGetInstallInfo function and returns the items from ADS\_MGMT\_INSTALL\_INFO.

Example

EXECUTE PROCEDURE sp\_mgGetInstallInfo();

See Also

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.htm)

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.htm)