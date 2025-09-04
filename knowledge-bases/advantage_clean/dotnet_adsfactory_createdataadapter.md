---
title: Dotnet Adsfactory Createdataadapter
slug: dotnet_adsfactory_createdataadapter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_createdataadapter.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 245c7e0593ad26cb28e90aa2202edc1caf3cf89a
---

# Dotnet Adsfactory Createdataadapter

AdsFactory.CreateDataAdapter

AdsFactory.CreateDataAdapter

Advantage .NET Data Provider

| AdsFactory.CreateDataAdapter  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsDataAdapter object as a strongly typed DbDataAdapter instance.

public DbDataAdapter CreateDataAdapter();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbDataAdapter adsAdapter = adsFact.CreateDataAdapter();

See Also

[AdsDataAdapter](dotnet_adsdataadapter.md)
