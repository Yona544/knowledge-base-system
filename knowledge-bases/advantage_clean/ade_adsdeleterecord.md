---
title: Ade Adsdeleterecord
slug: ade_adsdeleterecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsdeleterecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d60eb7dde8d98c198858b5470d900ec77d6927af
---

# Ade Adsdeleterecord

AdsDeleteRecord

TAdsTable.AdsDeleteRecord

Advantage TDataSet Descendant

| TAdsTable.AdsDeleteRecord  Advantage TDataSet Descendant |  |  |  |  |

Marks the current record in the given table as deleted.

Syntax

procedure AdsDeleteRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: Delete. See your Delphi documentation for more information about this native Delphi method.

Description

In DBF tables, AdsDeleteRecord works with the current record. AdsDeleteRecord does not actually remove the current record from the DBF table. The record is marked as deleted in the first byte of the record image. The record can be recalled using AdsRecallRecord. Query the deleted status of a record by using AdsIsRecordDeleted. Deleted records can be removed from tables completely by using [AdsPackTable](ade_adspacktable.md).

In Advantage proprietary ADT tables, AdsDeleteRecord will permanently delete the current record. The record cannot be recalled using AdsRecallRecord after the record has been written.

Note Deleted ADT records are automatically placed in a record re-use list. Because of this, they are unlocked by the server even if the user has an explicit lock on the record.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.Delete;

See Also

[AdsIsRecordDeleted](ade_adsisrecorddeleted.md)

[AdsPackTable](ade_adspacktable.md)

[AdsRecallRecord](ade_adsrecallrecord.md)
