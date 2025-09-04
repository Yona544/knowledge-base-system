---
title: Dotnet Adsextendedreader Getindexnames
slug: dotnet_adsextendedreader_getindexnames
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_getindexnames.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5115293e144f49309c3f6b9c695adf8e788ba548
---

# Dotnet Adsextendedreader Getindexnames

AdsExtendedReader.GetIndexNames

AdsExtendedReader.GetIndexNames

Advantage .NET Data Provider

| AdsExtendedReader.GetIndexNames  Advantage .NET Data Provider |  |  |  |  |

Returns an object array of index names for the given table.

public object[] GetIndexNames(); // (I) Name of file for new index order.

Remarks

The index names are returned in the order they were opened. For CDX and ADI indexes, the index names are returned in the order they were created within the index file.

See Also

[OpenIndex](dotnet_adsextendedreader_openindex.md)

[ActiveIndex](dotnet_adsextendedreader_activeindex.md)
