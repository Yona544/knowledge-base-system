---
title: Dotnet Adsextendedreader Copytablestructure
slug: dotnet_adsextendedreader_copytablestructure
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_copytablestructure.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3a270a087ac82398b2ec098f922107f151ff04e4
---

# Dotnet Adsextendedreader Copytablestructure

AdsExtendedReader.CopyTableStructure

AdsExtendedReader.CopyTableStructure

Advantage .NET Data Provider

| AdsExtendedReader.CopyTableStructure  Advantage .NET Data Provider |  |  |  |  |

Creates a new table with the given name having the same structure as the table opened with this reader.

public void CopyTableStructure( String strFile );

Remarks

The table created does not contain records, but has field structure identical to the original table. Indexes are not copied by CopyTableStructure. The resulting table must be opened by the application after the copy is performed before the application can use the table.

See Also

[CopyTable](dotnet_adsextendedreader_copytable.md)

[ConvertTable](dotnet_adsextendedreader_converttable.md)
