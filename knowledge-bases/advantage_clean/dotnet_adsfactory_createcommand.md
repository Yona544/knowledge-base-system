---
title: Dotnet Adsfactory Createcommand
slug: dotnet_adsfactory_createcommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_createcommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 30b9602b27bd4beeafae960cc77938fc14f6e4ab
---

# Dotnet Adsfactory Createcommand

AdsFactory.CreateCommand

AdsFactory.CreateCommand

Advantage .NET Data Provider

| AdsFactory.CreateCommand  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsCommand object as a strongly typed DbCommand instance.

public DbCommand CreateCommand();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbCommand adsCmd = adsFact.CreateCommand();

See Also

[AdsCommand](dotnet_adscommand.md)
