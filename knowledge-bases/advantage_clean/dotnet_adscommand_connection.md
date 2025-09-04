---
title: Dotnet Adscommand Connection
slug: dotnet_adscommand_connection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_connection.htm
source: Advantage CHM
tags:
  - dotnet
checksum: a66a237c4b8fd31e1b43b1fb756fd0652e71cbda
---

# Dotnet Adscommand Connection

AdsCommand.Connection

AdsCommand.Connection

Advantage .NET Data Provider

| AdsCommand.Connection  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the [AdsConnection](dotnet_adsconnection.md) used by this instance of the AdsCommand

public AdsConnection Connection {get; set;}

Remarks

If you set Connection while the command object has an open reader, AdsCommand will throw an InvalidOperationException.

See Also

[AdsConnection](dotnet_adsconnection.md)
