---
title: Dotnet Adsextendedreader Isindexcustom
slug: dotnet_adsextendedreader_isindexcustom
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_isindexcustom.htm
source: Advantage CHM
tags:
  - dotnet
checksum: fedbd3d765b9ff014f9e90d3a5d51e5b42abfdec
---

# Dotnet Adsextendedreader Isindexcustom

AdsExtendedReader.IsIndexCustom

AdsExtendedReader.IsIndexCustom

Advantage .NET Data Provider

| AdsExtendedReader.IsIndexCustom  Advantage .NET Data Provider |  |  |  |  |

Tests the active index to determine if it is a custom index.

public bool IsIndexCustom{ get; }

Remarks

This property returns true if the current index order is a custom index. Custom indexes are indexes that are not maintained by Advantage. An application must add and delete the keys. The Advantage .NET Data Provider does not provide the means to create or maintain custom indexes.

See Also

[AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.md)
