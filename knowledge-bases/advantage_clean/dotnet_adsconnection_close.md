---
title: Dotnet Adsconnection Close
slug: dotnet_adsconnection_close
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_close.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 92948cf58ba5e32159e288215791c0bf8efbf93d
---

# Dotnet Adsconnection Close

AdsConnection.Close

AdsConnection.Close

Advantage .NET Data Provider

| AdsConnection.Close  Advantage .NET Data Provider |  |  |  |  |

Closes the connection to the database.

public void Close();

Remarks

The Close method rolls back any pending transactions. It then returns the connection to the [connection pool](dotnet_advantage_net_data_provider_and_connection_pooling.md), or closes the connection if connection pooling is disabled (pooling=false).

An application can call Close more than one time. No exception is generated.

See Also

[AdsConnection.Open](dotnet_adsconnection_open.md)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)
