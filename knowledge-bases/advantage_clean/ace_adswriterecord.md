---
title: Ace Adswriterecord
slug: ace_adswriterecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adswriterecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9423428dcf6d44b4d193d4f43443a742e185753e
---

# Ace Adswriterecord

AdsWriteRecord

AdsWriteRecord

Advantage Client Engine

| AdsWriteRecord  Advantage Client Engine |  |  |  |  |

Writes any changes in the current record.

Syntax

| UNSIGNED32 | AdsWriteRecord (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table or cursor. |

Remarks

AdsWriteRecord flushes any data changes to the Advantage server. If an implicit lock is held on the record, calling this function will release it.

Example

[Click Here](ace_examples.md#adswriterecordexample)

See Also

[AdsWriteAllRecords](ace_adswriteallrecords.md)
