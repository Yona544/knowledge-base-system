---
title: Ade Adsrecallrecord
slug: ade_adsrecallrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsrecallrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6835163af408bc5e77a30bc14117064987e036b3
---

# Ade Adsrecallrecord

AdsRecallRecord

TAdsTable/TAdsQuery.AdsRecallRecord

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsRecallRecord  Advantage TDataSet Descendant |  |  |  |  |

Restores the current record in the given DBF dataset to normal visibility.

Syntax

procedure AdsRecallRecord;

Description

Calling AdsRecallRecord on a deleted record in a DBF dataset will clear the deleted flag in the first byte of the record.

Note AdsRecallRecord has little effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved nor can they be recalled by a client application. If AdsRecallRecord is called after a call to AdsDeleteRecord and before the record is written, the record will not be deleted. Once a deleted record has been written either through a call to [AdsWriteRecord](ade_adswriterecord.md) or implicitly through some record movement, that record cannot be recalled.

Example

AdsSettings1.ShowDeleted := TRUE;

AdsTable1.Next;

if AdsTable1.AdsIsRecordDeleted(0) then

AdsTable1.AdsRecallRecord;

See Also

[AdsDeleteRecord](ade_adsdeleterecord.md)

[AdsIsRecordDeleted](ade_adsisrecorddeleted.md)
