---
title: Ace Adsgetrecordlength
slug: ace_adsgetrecordlength
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetrecordlength.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 8361b0009672c3886b59c8e1a541073670f3c256
---

# Ace Adsgetrecordlength

AdsGetRecordLength

AdsGetRecordLength

Advantage Client Engine

| AdsGetRecordLength  Advantage Client Engine |  |  |  |  |

Retrieves the record size for the given table

Syntax

| UNSIGNED32 | AdsGetRecordLength (ADSHANDLE hTable,  UNSIGNED32 \*pulSize); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pulSize (O) | Return size of record. This includes the deleted byte as well. |

Remarks

The record size returned includes space for the deleted byte for DBF table records. For ADT records, this record size will include 5 extra bytes used internally by Advantage. This length may not reflect the actual amount of data accessible for this record if the table includes variable-length fields.

Example

[Click Here](ace_examples.md#adsgetrecordlengthexample)

See Also

[AdsGetRecord](ace_adsgetrecord.md)

[AdsGetRecordNum](ace_adsgetrecordnum.md)
