---
title: Dotnet Adsfactory Createcommandbuilder
slug: dotnet_adsfactory_createcommandbuilder
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsfactory_createcommandbuilder.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 217c82aa0934ac3cc5e73133c900cc23d6d21999
---

# Dotnet Adsfactory Createcommandbuilder

AdsFactory.CreateCommandBuilder

AdsFactory.CreateCommandBuilder

Advantage .NET Data Provider

| AdsFactory.CreateCommandBuilder  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsCommandBuilder object as a strongly typed DbCommandBuilder instance.

public DbCommandBuilder CreateCommandBuilder();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbCommandBuilder adsCmdBldr = adsFact.CreateCommandBuilder();

See Also

[AdsCommandBuilder](dotnet_adscommandbuilder.md)
