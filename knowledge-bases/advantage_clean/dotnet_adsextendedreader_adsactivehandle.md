---
title: Dotnet Adsextendedreader Adsactivehandle
slug: dotnet_adsextendedreader_adsactivehandle
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_adsactivehandle.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ddf09ca8745431defca3208a9e34ebf8bf0cfad4
---

# Dotnet Adsextendedreader Adsactivehandle

AdsExtendedReader.AdsActiveHandle

AdsExtendedReader.AdsActiveHandle

Advantage .NET Data Provider

| AdsExtendedReader.AdsActiveHandle  Advantage .NET Data Provider |  |  |  |  |

Gets the handle of the table, cursor, or index.

public IntPtr AdsActiveHandle{ get; }

Remarks

This property can be used to retrieve the active table, cursor, or index handle being used by AdsExtendedReader. If there is an active index, it will return the Advantage Client Engine index handle associated with that index, otherwise, it will return the same value as AdsExltendedReader.AdsHandle.

See Also

[AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.md)

[AdsExtendedReader.AdsHandle](dotnet_adsextendedreader_adshandle.md)
