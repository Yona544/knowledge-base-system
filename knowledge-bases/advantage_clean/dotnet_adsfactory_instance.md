---
title: Dotnet Adsfactory Instance
slug: dotnet_adsfactory_instance
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_instance.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 80164e405e09625f5036ac63a87a98dc8538aa7d
---

# Dotnet Adsfactory Instance

AdsFactory.Instance

AdsFactory.Instance

Advantage .NET Data Provider

| AdsFactory.Instance  Advantage .NET Data Provider |  |  |  |  |

Gets an instance of the AdsFactory. This can be used to retrieve strongly typed data objects.

public static readonly AdsFactory Instance;

Remarks

An application has a single instance of AdsFactory. It can be retrieved via the Instance field of the AdsFactory class. It can also be retrieved by calling DbProviderFactories.GetFactory().

Example

AdsFactory adsFact = AdsFactory.Instance;

DbConnection adsConn = adsFact.CreateConnection();
