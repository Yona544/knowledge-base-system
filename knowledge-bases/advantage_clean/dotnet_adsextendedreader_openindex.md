---
title: Dotnet Adsextendedreader Openindex
slug: dotnet_adsextendedreader_openindex
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_openindex.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 86078596c95006234bbe074fc2ad084578e9c51b
---

# Dotnet Adsextendedreader Openindex

AdsExtendedReader.OpenIndex

AdsExtendedReader.OpenIndex

Advantage .NET Data Provider

| AdsExtendedReader.OpenIndex  Advantage .NET Data Provider |  |  |  |  |

Opens an index file and associates all index orders in the file with the open table.

public void OpenIndex( string strFileName );

Remarks

OpenIndex retrieves all handles of index orders in the given index file. If the index file is NOT a compound index (CDX or ADI), then it will have only one index order. If the index file is a compound CDX or ADI index, however, more than one index order handle may be returned.

Non-compact IDX files are not supported.

Opening an index does not change the current record.

See Also

[GetIndexNames](dotnet_adsextendedreader_getindexnames.md)

[CreateIndex](dotnet_adsextendedreader_createindex.md)

[ActiveIndex](dotnet_adsextendedreader_activeindex.md)
