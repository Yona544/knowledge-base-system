---
title: Ace Adsrecallallrecords
slug: ace_adsrecallallrecords
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsrecallallrecords.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8853343e3342738c1443432184d263c03cdc3e0c
---

# Ace Adsrecallallrecords

AdsRecallAllRecords

AdsRecallAllRecords

Advantage Client Engine

| AdsRecallAllRecords  Advantage Client Engine |  |  |  |  |

Recalls all deleted records in a table.

Syntax

| UNSIGNED32 | AdsRecallAllRecords (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of a table. |

Remarks

AdsRecallAllRecords loops through each record in the given table and recalls all deleted records. This API uses slightly lower level functions and thus can recall more records (for ADTs) than [AdsRecallRecord](ace_adsrecallrecord.md). This operation requires exclusive access to the table, specified during the open. To ensure the integrity of the table header and all associated indexes, AdsRecallAllRecords performs a pack of the table after recalling all deleted records. For this reason, all associated indexes of this table must be opened to remain logically correct. See [AdsPackTable](ace_adspacktable.md) for more information.

Note AdsRecallAllRecords can only recall records still in the re-use list (for ADTs). Once a record buffer is re-used, it can never be recalled.

See Also

[AdsRecall Record](ace_adsrecallrecord.md)

[AdsDeleteRecord](ace_adsdeleterecord.md)
