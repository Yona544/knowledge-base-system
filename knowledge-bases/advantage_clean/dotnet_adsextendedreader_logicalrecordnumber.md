---
title: Dotnet Adsextendedreader Logicalrecordnumber
slug: dotnet_adsextendedreader_logicalrecordnumber
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_logicalrecordnumber.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 9896966ee1afdefb20db32e15d38388c0ceb3eea
---

# Dotnet Adsextendedreader Logicalrecordnumber

AdsExtendedReader.LogicalRecordNumber

AdsExtendedReader.LogicalRecordNumber

Advantage .NET Data Provider

| AdsExtendedReader.LogicalRecordNumber  Advantage .NET Data Provider |  |  |  |  |

Retrieves the current logical record number.

public int LogicalRecordNumber{ get; }

Remarks

This property can be used to retrieve a record number that logically takes into account filters ([AdsExtendedReader.Filter](dotnet_adsextendedreader_filter.md)), ranges ([AdsExtendedReader.SetRange](dotnet_adsextendedreader_setrange.md)), and deleted records. If an index is active ([AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.md)), then the value retrieved will be the key number obeying filters and ranges.

Note This property may result in skipping through every record in a table to obtain the count and can be very slow.

See Also

[RecordNumber](dotnet_adsextendedreader_recordnumber.md)
