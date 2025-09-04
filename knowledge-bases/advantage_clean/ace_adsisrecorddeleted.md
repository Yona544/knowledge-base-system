---
title: Ace Adsisrecorddeleted
slug: ace_adsisrecorddeleted
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisrecorddeleted.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e8a5b02a6af28501423fa58d29405871fef77fe1
---

# Ace Adsisrecorddeleted

AdsIsRecordDeleted

AdsIsRecordDeleted

Advantage Client Engine

| AdsIsRecordDeleted  Advantage Client Engine |  |  |  |  |

Determines the deleted status of the current record in a DBF table.

Syntax

| UNSIGNED32 | AdsIsRecordDeleted (ADSHANDLE hTable,  UNSIGNED16 \*pbDeleted); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pbDeleted (O) | Return True if the current record is marked for deletion, False if not. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

The first byte of every record in a DBF table is reserved for use as a deleted byte. This byte signals whether the record is deleted and/or encrypted. The result of this function can be used to implement a recycling algorithm for deleted records, or a periodic [AdsPackTable](ace_adspacktable.md) can be used to remove deleted records from the table.

Note AdsIsRecordDeleted will generally return False in the pbDeleted parameter for Advantage proprietary ADT tables. Records that are deleted in ADT tables are permanently deleted and can never be retrieved by a client application once they have been written. It is possible to call AdsIsRecordDeleted just after calling [AdsDeleteRecord](ace_adsdeleterecord.md) and before the record is written. This function will return True in that case.

Example

[Click Here](ace_examples.md#adsisrecorddeletedexample)

See Also

[AdsDeleteRecord](ace_adsdeleterecord.md)

[AdsRecallRecord](ace_adsrecallrecord.md)

[AdsPackTable](ace_adspacktable.md)

[AdsShowDeleted](ace_adsshowdeleted.md)
