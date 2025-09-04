---
title: Dotnet Adsfactory Createconnectionstringbuilder
slug: dotnet_adsfactory_createconnectionstringbuilder
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_createconnectionstringbuilder.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c2a66a09b3bf1f0c7c876f8748f3103ec3557acd
---

# Dotnet Adsfactory Createconnectionstringbuilder

AdsFactory.CreateConnectionStringBuilder

AdsFactory.CreateConnectionStringBuilder

Advantage .NET Data Provider

| AdsFactory.CreateConnectionStringBuilder  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsConnectionStringBuilder object as a strongly typed DbConnectionStringBuilder instance.

public DbConnectionStringBuilder CreateConnectionStringBuilder();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbConnectionStringBuilder adsCSBldr =

adsFact.CreateConnectionStringBuilder();

See Also

[AdsConnectionStringBuilder](dotnet_adsconnectionstringbuilder_class.md)
