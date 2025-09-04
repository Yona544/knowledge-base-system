---
title: Dotnet Adsextendedreader Recallrecord
slug: dotnet_adsextendedreader_recallrecord
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_recallrecord.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 83c85b471752e865afbe1046cf35127a65a962ca
---

# Dotnet Adsextendedreader Recallrecord

AdsExtendedReader.RecallRecord

AdsExtendedReader.RecallRecord

Advantage .NET Data Provider

| AdsExtendedReader.RecallRecord  Advantage .NET Data Provider |  |  |  |  |

Restores the current record in a DBF table to normal visibility.

public void RecallRecord();

Remarks

Calling RecallRecord on a deleted record in a DBF table will clear the deleted flag in the first byte of the record.

Note RecallRecord has little effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved nor can they be recalled by a client application. If RecallRecord is called after a call to DeleteRecord and before the record is written, then the record will not be deleted. Once a deleted record has been written either through a call to WriteRecord or implicitly through some record movement, then that record cannot be recalled.

See Also

[DeleteRecord](dotnet_adsextendedreader_deleterecord.md)

[IsRecordDeleted](dotnet_adsextendedreader_isrecorddeleted.md)
