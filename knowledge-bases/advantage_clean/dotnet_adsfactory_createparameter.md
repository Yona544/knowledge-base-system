---
title: Dotnet Adsfactory Createparameter
slug: dotnet_adsfactory_createparameter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_createparameter.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d9b733e84bae6c6229c0dda1db8c2874de91f545
---

# Dotnet Adsfactory Createparameter

AdsFactory.CreateParameter

AdsFactory.CreateParameter

Advantage .NET Data Provider

| AdsFactory.CreateParameter  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsParameter object as a strongly typed DbParameter instance.

public DbParameter CreateParameter();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbParameter adsParam = adsFact.CreateParameter();

See Also

[AdsParameter](dotnet_adsparameter.md)
