---
title: Dotnet Adsconnection Servertype
slug: dotnet_adsconnection_servertype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_servertype.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 6a89e06457037a29c267fab6ac6a15296f4d11a7
---

# Dotnet Adsconnection Servertype

AdsConnection.ServerType

AdsConnection.ServerType

Advantage .NET Data Provider

| AdsConnection.ServerType  Advantage .NET Data Provider |  |  |  |  |

Returns the type of Advantage Database Server a connection uses.

public string ServerType{ get; }

Remarks

ServerType returns the type of connection being used as a string. Values returned include:

| "REMOTE" | The Advantage Database Server for Windows or the Advantage Database Server for Linux is in use. |
| "LOCAL" | The Advantage Local Server is being used by this connection. |
| "AIS" | The connection is using an Advantage Internet Server. |

It is possible to have connections to each type of Advantage server in one application. If the connection is not open, ServerType will return a string based on the ServerType value in the ConnectionString.

See Also

[ConnectionString](dotnet_adsconnection_connectionstring.md)
