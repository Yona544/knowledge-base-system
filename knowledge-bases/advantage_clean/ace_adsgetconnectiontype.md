---
title: Ace Adsgetconnectiontype
slug: ace_adsgetconnectiontype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetconnectiontype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5e801dd573ef401b341ce8fda20c3b899c384c89
---

# Ace Adsgetconnectiontype

AdsGetConnectionType

AdsGetConnectionType

Advantage Client Engine

| AdsGetConnectionType  Advantage Client Engine |  |  |  |  |

Returns the type of Advantage Database Server a connection uses.

Syntax

| UNSIGNED32 | AdsGetConnectionType (ADSHANDLE hConnect,  UNSIGNED16 \*pusConnectType); |

Parameters

| hConnect (I) | Connection handle |
| pucConnectType (O) | Type of Advantage Server that connection uses, either ADS\_REMOTE\_SERVER, ADS\_AIS\_SERVER, or ADS\_LOCAL\_SERVER |

Remarks

If AdsGetConnectionType returns ADS\_AIS\_SERVER, the connection is using an Advantage Internet Server.

A return value of ADS\_REMOTE\_SERVER indicates the Advantage Database Server for Windows or the Advantage Database Server for Linux is in use.

ADS\_LOCAL\_SERVER indicates the [Advantage Local Server](master_advantage_local_server.md) is being used by this connection. It is possible to have connections to each type of Advantage server in one application.

Example

None.

See Also

[AdsConnect](ace_adsconnect.md)

[AdsGetTableConnection](ace_adsgettableconnection.md)

[AdsIsServerLoaded](ace_adsisserverloaded.md)
