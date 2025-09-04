---
title: Ace Adssetservertype
slug: ace_adssetservertype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetservertype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 18ec5d51f6ca742fc7e2fca4cd49eb9844dec313
---

# Ace Adssetservertype

AdsSetServerType

AdsSetServerType

Advantage Client Engine

| AdsSetServerType  Advantage Client Engine |  |  |  |  |

Controls the types of Advantage Database Servers to which the client application can connect.

Syntax

| UNSIGNED32 | AdsSetServerType (UNSIGNED16 usServerType); |

Parameters

| usServerType (I) | Bitmask of server types to allow client connections to. Options are ADS\_REMOTE\_SERVER, ADS\_AIS\_SERVER, and ADS\_LOCAL\_SERVER. The default is ADS\_REMOTE\_SERVER logically ORd with ADS\_AIS\_SERVER. |

Remarks

AdsSetServerType determines which types of Advantage servers the client application can use. The options available are ADS\_REMOTE\_SERVER. This option refers to the Advantage Database Server for Windows or the Advantage Database Server for Linux. ADS\_LOCAL\_SERVER references the [Advantage Local Server](master_advantage_local_server.md) and ADS\_AIS\_SERVER designates the Advantage Internet Server. These options can be logically ORd together to allow the client application to connect to any combination of server types. If multiple server types are specified, then the Advantage Client Engine uses the following precedence when attempting to connect: highest priority is given to ADS\_REMOTE\_SERVER, second priority to ADS\_AIS\_SERVER, and lowest priority to ADS\_LOCAL\_SERVER. For example, if the option to AdsSetServerType is ADS\_REMOTE\_SERVER ORd with ADS\_LOCAL\_SERVER, all connections to Advantage servers will be true client/server connections. Advantage Local Server would only be used for connections to servers without the Advantage Database Server running due to the lower precedence of the local server. If ADS\_REMOTE\_SERVER and ADS\_LOCAL\_SERVER have both been selected, it may take two seconds to default to the Advantage Local Server if the Advantage Database Server is not running on the file server.

AdsSetServerType is a global setting that affects the behavior of the entire application.

Example

None.

See Also

[AdsConnect](ace_adsconnect.md)

[AdsGetConnectionType](ace_adsgetconnectiontype.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsIsServerLoaded](ace_adsisserverloaded.md)
