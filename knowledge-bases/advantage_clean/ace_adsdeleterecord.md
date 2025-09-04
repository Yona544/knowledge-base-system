---
title: Ace Adsdeleterecord
slug: ace_adsdeleterecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdeleterecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0a8d3e9b5c13400d2a89c99559ce3ea6428cc5b1
---

# Ace Adsdeleterecord

AdsDeleteRecord

AdsDeleteRecord

Advantage Client Engine

| AdsDeleteRecord  Advantage Client Engine |  |  |  |  |

Marks the current record in the given table as deleted.

Syntax

| UNSIGNED32 | AdsDeleteRecord (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor. |

Remarks

In DBF tables, AdsDeleteRecord does not actually remove the current record from the table. The record is marked in the first byte of the record image as deleted. The record can be recalled using [AdsRecallRecord](ace_adsrecallrecord.md). Query the deleted status of a record by using [AdsIsRecordDeleted](ace_adsisrecorddeleted.md). Deleted records can be removed from tables completely by using [AdsPackTable](ace_adspacktable.md).

In Advantage proprietary ADT tables, AdsDeleteRecord will permanently delete the current record. The record cannot be recalled using [AdsRecallRecord](ace_adsrecallrecord.md) after the record has been written.

Note Deleted ADT records are automatically placed in a record re-use list. Because of this, the server unlocks them even if the user has an explicit lock on the record.

Example

[Click Here](ace_examples.md#adsdeleterecordexample)

See Also

[AdsRecallRecord](ace_adsrecallrecord.md)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.md)

[AdsPackTable](ace_adspacktable.md)

[AdsAtEOF](ace_adsateof.md)
