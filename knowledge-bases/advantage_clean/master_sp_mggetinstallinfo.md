---
title: Master Sp Mggetinstallinfo
slug: master_sp_mggetinstallinfo
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetinstallinfo.htm
source: Advantage CHM
tags:
  - master
checksum: 77712f558b3a28a01400d06b4499c76ad5303bf9
---

# Master Sp Mggetinstallinfo

sp\_mgGetInstallInfo

sp\_mgGetInstallInfo

Advantage SQL Engine

| sp\_mgGetInstallInfo  Advantage SQL Engine |  |  |  |  |

Returns Advantage Database Server Installation information.

Syntax

EXECUTE PROCEDURE sp\_mgGetInstallInfo()

Parameters

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

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.md)

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.md)
