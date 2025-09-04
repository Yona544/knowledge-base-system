---
title: Dotnet Adsextendedreader Isrecorddeleted
slug: dotnet_adsextendedreader_isrecorddeleted
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_isrecorddeleted.htm
source: Advantage CHM
tags:
  - dotnet
checksum: f616338601a53fe4fd31193873ee7aeb97edab3d
---

# Dotnet Adsextendedreader Isrecorddeleted

AdsExtendedReader.IsRecordDeleted

AdsExtendedReader.IsRecordDeleted

Advantage .NET Data Provider

| AdsExtendedReader.IsRecordDeleted  Advantage .NET Data Provider |  |  |  |  |

Tests the deleted status of the current record.

public bool IsRecordDeleted();

 

Remarks

The first byte of every record in a DBF table is reserved for use as a deleted byte. This byte signals whether the record is deleted. This method returns true if the record is marked as deleted.

Note IsRecordDeleted will generally return false for Advantage proprietary ADT tables. Records that are deleted in ADT tables are permanently deleted and can never be retrieved by a client application once they have been written. It is possible to call IsRecordDeleted just after calling DeleteRecord and before the record is written. This function will return true in that case.

See Also

[DeleteRecord](dotnet_adsextendedreader_deleterecord.md)

[RecallRecord](dotnet_adsextendedreader_recallrecord.md)

[PackTable](dotnet_adsextendedreader_packtable.md)
