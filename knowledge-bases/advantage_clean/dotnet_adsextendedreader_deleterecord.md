---
title: Dotnet Adsextendedreader Deleterecord
slug: dotnet_adsextendedreader_deleterecord
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_deleterecord.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 6d9729e74b3d4186285a2fc398385d54ff254993
---

# Dotnet Adsextendedreader Deleterecord

AdsExtendedReader.DeleteRecord

AdsExtendedReader.DeleteRecord

Advantage .NET Data Provider

| AdsExtendedReader.DeleteRecord  Advantage .NET Data Provider |  |  |  |  |

Marks the current record as deleted.

public void DeleteRecord();

Remarks

In DBF tables, DeleteRecord does not actually remove the current record from the table. The record is marked in the first byte of the record image as deleted. The record can be recalled using RecallRecord. Deleted records can be removed from tables completely by using PackTable.

In Advantage proprietary ADT tables, DeleteRecord will permanently delete the current record. The record cannot be recalled using RecallRecord after the record has been written.

Note Deleted ADT records are automatically placed in a record re-use list. Because of this, the server unlocks them even if the user has an explicit lock on the record.

See Also

[RecallRecord](dotnet_adsextendedreader_recallrecord.md)

[IsRecordDeleted](dotnet_adsextendedreader_isrecorddeleted.md)
