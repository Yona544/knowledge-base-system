---
title: Dotnet Adsfactory Createconnection
slug: dotnet_adsfactory_createconnection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_createconnection.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1d7c221e50e6fb54987f9231278a30839d314822
---

# Dotnet Adsfactory Createconnection

AdsFactory.CreateConnection

AdsFactory.CreateConnection

Advantage .NET Data Provider

| AdsFactory.CreateConnection  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsConnection object as a strongly typed DbConnection instance.

public DbConnection CreateConnection();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbConnection adsConn = adsFact.CreateConnection();

See Also

[AdsConnection](dotnet_adsconnection.md)
