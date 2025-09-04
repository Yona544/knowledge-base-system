---
title: Ace Adsrecallrecord
slug: ace_adsrecallrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsrecallrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b973cffb9fc82051134ab7fa5be7a9a2e8710a08
---

# Ace Adsrecallrecord

AdsRecallRecord

AdsRecallRecord

Advantage Client Engine

| AdsRecallRecord  Advantage Client Engine |  |  |  |  |

Restores the current record in the given DBF table to normal visibility.

Syntax

| UNSIGNED32 | AdsRecallRecord (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor. |

Remarks

Calling AdsRecallRecord on a deleted record in a DBF table will clear the deleted flag in the first byte of the record.

Note AdsRecallRecord has little effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved nor can they be recalled by a client application. If AdsRecallRecord is called after a call to AdsDeleteRecord and before the record is written, then the record will not be deleted. Once a deleted record has been written either through a call to [AdsWriteRecord](ace_adswriterecord.md) or implicitly through some record movement, then that record cannot be recalled.

Example

[Click Here](ace_examples.md#adsrecallrecordexample)

See Also

[AdsShowDeleted](ace_adsshowdeleted.md)

[AdsDeleteRecord](ace_adsdeleterecord.md)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.md)
