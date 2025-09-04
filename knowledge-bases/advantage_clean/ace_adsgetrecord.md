---
title: Ace Adsgetrecord
slug: ace_adsgetrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 6f33fc58daa99ba4f506cb1145fb781c2be0ab1c
---

# Ace Adsgetrecord

AdsGetRecord

AdsGetRecord

Advantage Client Engine

| AdsGetRecord  Advantage Client Engine |  |  |  |  |

Returns the current record as a single raw data buffer.

Syntax

| UNSIGNED32 | AdsGetRecord (ADSHANDLE hTable,  UNSIGNED8 \*pucRec,  UNSIGNED32 \*pulLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucRec (O) | Return record contents in this buffer. |
| pulLen (I/O) | Length of given buffer on input, length of returned data on output. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

Use of AdsGetRecord is strongly discouraged, especially if there are memo fields or extended data types present in the table. It is much safer to use [AdsGetField](ace_adsgetfield.md) and related functions to read information from a record.

Example

[Click Here](ace_examples.md#adsgetrecordexample)

See Also

[AdsSetRecord](ace_adssetrecord.md)

[AdsGetField](ace_adsgetfield.md)
