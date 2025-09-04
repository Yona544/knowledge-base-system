---
title: Dotnet Adsextendedreader Lastautoinc
slug: dotnet_adsextendedreader_lastautoinc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_lastautoinc.htm
source: Advantage CHM
tags:
  - dotnet
checksum: e18667011cf23e63f9fc7c3d26b16aaf9f8eb831
---

# Dotnet Adsextendedreader Lastautoinc

AdsExtendedReader.LastAutoinc

AdsExtendedReader.LastAutoinc

Advantage .NET Data Provider

| AdsExtendedReader.LastAutoinc  Advantage .NET Data Provider |  |  |  |  |

Retrieves the last inserted autoinc value after an SQL INSERT or table append.

public int LastAutoinc{ get; }

Remarks

Returns the last inserted Autoinc value for the given handle. If no Autoinc value has been inserted or the table does not contain an Autoinc field then 0 is returned.

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.
