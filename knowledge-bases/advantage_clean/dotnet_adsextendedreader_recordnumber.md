---
title: Dotnet Adsextendedreader Recordnumber
slug: dotnet_adsextendedreader_recordnumber
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_recordnumber.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2ec7ea96c5c41c2d9318550e75f0ee1a99cdeb87
---

# Dotnet Adsextendedreader Recordnumber

AdsExtendedReader.RecordNumber

AdsExtendedReader.RecordNumber

Advantage .NET Data Provider

| AdsExtendedReader.RecordNumber  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the current record number.

public int RecordNumber{ get; set; }

Remarks

Each physical record in a table has a record number. The first physical record is number 1. All records, even deleted ones (in DBF tables), have record numbers. The only way to change record numbers in a table is to perform a [PackTable](dotnet_adsextendedreader_packtable.md).

RecordNumber ignores filters, indexes, and scopes. It sets the physical record number even if an index is active. If set to zero or a number greater than the total number of records, the client will be unpositioned (EOF and BOF will be set) and the current record number will be set to 0.

Note If setting the RecordNumber property and using the AdsExtendedReader.Read method, the Read method will skip FROM the record number that was set using the RecordNumber property, which means values read will be from the next record in the dataset, not the record explicitly set via RecordNumber.

See Also

[GetBookmark](dotnet_adsextendedreader_getbookmark.md)

[GotoBookmark](dotnet_adsextendedreader_gotobookmark.md)

[LogicalRecordNumber](dotnet_adsextendedreader_logicalrecordnumber.md)
