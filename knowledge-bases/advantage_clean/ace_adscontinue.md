---
title: Ace Adscontinue
slug: ace_adscontinue
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscontinue.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fa3ee37a2154e9ea3c8ad293ab77b89790beeb4c
---

# Ace Adscontinue

AdsContinue

AdsContinue

Advantage Client Engine

| AdsContinue  Advantage Client Engine |  |  |  |  |

Continues the locate command based on a previous call to [AdsLocate](ace_adslocate.md)

Syntax

| UNSIGNED32 | AdsContinue (ADSHANDLE hTable,  UNSIGNED16 \*pbFound); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pbFound (O) | Return True if record found. |

Remarks

AdsContinue continues searching for records that pass the condition specified in [AdsLocate](ace_adslocate.md) in the direction set by the AdsLocate function. If pbFound returns False, the table is positioned at EOF or BOF, depending on the direction of the AdsLocate.

AdsContinue performs a skip before evaluating the current record against the condition set in AdsLocate. It is unnecessary to explicitly call [AdsSkip](ace_adsskip.md) between an AdsLocate and an AdsContinue call or between successive AdsContinue calls.

Note Since each record is read from the server for comparison against the filter, it would be faster to use [AdsSetFilter](ace_adssetfilter.md) because the server would then perform the filtering.

Example

[Click Here](ace_examples.md#adscontinueexample)

See Also

[AdsLocate](ace_adslocate.md)

[AdsIsFound](ace_adsisfound.md)
