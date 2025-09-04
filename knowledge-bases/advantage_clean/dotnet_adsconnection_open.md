---
title: Dotnet Adsconnection Open
slug: dotnet_adsconnection_open
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_open.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2e520fcd341f58e376ca537b4966a68cc2c26ec6
---

# Dotnet Adsconnection Open

AdsConnection.Open

AdsConnection.Open

Advantage .NET Data Provider

| AdsConnection.Open  Advantage .NET Data Provider |  |  |  |  |

Opens a database connection with the property settings specified by the [ConnectionString](dotnet_adsconnection_connectionstring.md).

public void Open();

Remarks

This method opens a connection to the database or retrieves an open connection from the [connection pool](dotnet_advantage_net_data_provider_and_connection_pooling.md) (if pooling is enabled). Otherwise, it establishes a new connection. If pooling is on and the maximum pool size (property "Max Pool Size") is exceeded, an InvalidOperationException will be thrown.

See Also

[ConnectionString](dotnet_adsconnection_connectionstring.md)

[Close](dotnet_adsconnection_close.md)
