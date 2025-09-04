---
title: Ace Adsatbof
slug: ace_adsatbof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsatbof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 86690e9df4c08c1c520fba733e1c1534e3d63b1d
---

# Ace Adsatbof

AdsAtBOF

AdsAtBOF

Advantage Client Engine

| AdsAtBOF  Advantage Client Engine |  |  |  |  |

Determines if the current position is at the beginning of the table

Syntax

| UNSIGNED32 | AdsAtBOF (ADSHANDLE hTable,  UNSIGNED16 \*pbBOF); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pbBof (O) | Set to True if at BOF. |

Remarks

The BOF flag (Beginning Of File) indicates that the table is positioned at the top of the table on a virtual record. When BOF is True, the record number is zero (0). Data values cannot be retrieved because there is no physical record. The BOF flag is set after an [AdsSkip](ace_adsskip.md) call with a negative number that skips back past the first record in the table, or if there are no records currently visible. When located at BOF and there are no visible records, skipping forward 1 (one) will position at the first logical record in the table, or another movement function can be used to position.

Example

[Click Here](ace_examples.md#adsatbofexample)

See Also

[AdsAtEOF](ace_adsateof.md)

[AdsSkip](ace_adsskip.md)
