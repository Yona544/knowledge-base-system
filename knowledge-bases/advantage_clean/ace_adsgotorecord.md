---
title: Ace Adsgotorecord
slug: ace_adsgotorecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgotorecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a1c0f12c6f6daa0e2401426085f8eba75b3269b6
---

# Ace Adsgotorecord

AdsGotoRecord

AdsGotoRecord

Advantage Client Engine

| AdsGotoRecord  Advantage Client Engine |  |  |  |  |

Positions the given table to the given record number

Syntax

| UNSIGNED32 | AdsGotoRecord (ADSHANDLE hTable,  UNSIGNED32 ulRec); |

Parameters

| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number. |

Remarks

AdsGotoRecord ignores filters, relations, and scopes. If ulRec is zero, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to 0. If ulRec is greater than the number of records in the table, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to the number of records in the table + 1.

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

Example

[Click Here](ace_examples.md#adsgotorecordexample)

See Also

[AdsGotoBottom](ace_adsgotobottom.md)

[AdsGotoTop](ace_adsgototop.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)

[AdsGetRecordCount](ace_adsgetrecordcount.md)

[AdsSkip](ace_adsskip.md)

[AdsWriteRecord](ace_adswriterecord.md)
