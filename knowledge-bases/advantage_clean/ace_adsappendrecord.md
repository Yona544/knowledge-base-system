---
title: Ace Adsappendrecord
slug: ace_adsappendrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsappendrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8395c900bbd072ca66f035ab891730f772fc2b3f
---

# Ace Adsappendrecord

AdsAppendRecord

AdsAppendRecord

Advantage Client Engine

| AdsAppendRecord  Advantage Client Engine |  |  |  |  |

Appends an empty record to the end of the given table.

Syntax

| UNSIGNED32 | AdsAppendRecord (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor. |

Remarks

AdsAppendRecord appends a blank record to the end of the table, locks the record, and positions the table to the new record. Changes are written when the user moves off of the appended record or calls [AdsWriteRecord](ace_adswriterecord.md). Transactions have some affect on appending records; see [Advantage Transaction Processing](master_transaction_processing_system.md) for more information on appends during transactions.

Note With ADT tables, Advantage implements a record re-use algorithm that recycles records that have been deleted ([AdsDeleteRecord](ace_adsdeleterecord.md)). This means that the newly appended record may not actually be at the end of the table. An application should not make any assumptions about the new record number.

Example

[Click Here](ace_examples.md#adsappendrecordexample)

See Also

[AdsDeleteRecord](ace_adsdeleterecord.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)
