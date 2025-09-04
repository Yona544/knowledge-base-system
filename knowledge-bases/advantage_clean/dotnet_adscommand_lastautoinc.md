---
title: Dotnet Adscommand Lastautoinc
slug: dotnet_adscommand_lastautoinc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_lastautoinc.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8c0f9bc19711e5ec9e1f9ad4617c99bcca304f59
---

# Dotnet Adscommand Lastautoinc

AdsCommand.LastAutoinc

AdsCommand.LastAutoinc

Advantage .NET Data Provider

| AdsCommand.LastAutoinc  Advantage .NET Data Provider |  |  |  |  |

Retrieves the last inserted autoinc value after an SQL INSERT or table append.

public int LastAutoinc{ get; }

Remarks

Returns the last inserted Autoinc value for the command object. If no Autoinc value has been inserted or the affected table does not contain an Autoinc field then 0 is returned.

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.
