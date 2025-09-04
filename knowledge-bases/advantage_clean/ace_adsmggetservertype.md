---
title: Ace Adsmggetservertype
slug: ace_adsmggetservertype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsmggetservertype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d2a93370edbf27f57e44da6c94e393ea8a98c46b
---

# Ace Adsmggetservertype

AdsMgGetServerType

AdsMgGetServerType

Advantage Client Engine

| AdsMgGetServerType  Advantage Client Engine |  |  |  |  |

Returns the Advantage server type of the current management API connection

Syntax

| UNSIGNED32 | AdsMgGetServerType ( ADSHANDLE hMgmtConnect,  UNSIGNED16 \*pusServerType ); |

Parameters

| hMgmtConnect (I) | Management API connection handle. |
| pusServerType (O) | Advantage server type of the current management API connection. |

Remarks

AdsMgGetServerType returns the Advantage server type of the current management connection.

If connected to the Advantage Database Server for Windows, ADS\_MGMT\_NT\_SERVER or ADS\_MGMT\_NT\_SERVER\_64\_BIT is returned.

If connected to the Advantage Local Server, ADS\_MGMT\_LOCAL\_SERVER is returned.

If connected to the Advantage Database Server for Linux, ADS\_MGMT\_LINUX\_SERVER or ADS\_MGMT\_LINUX\_SERVER\_64\_BIT is returned.

Example

[Click Here](ace_advantage_management_api_examples.md#adsmggetservertype_example)

See Also

[AdsMgConnect](ace_adsmgconnect.md)

[AdsGetConnectionType](ace_adsgetconnectiontype.md)
