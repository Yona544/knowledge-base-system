---
title: Ace Adsgetepoch
slug: ace_adsgetepoch
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetepoch.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d5061570b5afae597510c93391423c65c583ccf7
---

# Ace Adsgetepoch

AdsGetEpoch

AdsGetEpoch

Advantage Client Engine

| AdsGetEpoch  Advantage Client Engine |  |  |  |  |

Retrieves the current epoch setting

Syntax

| UNSIGNED32 | AdsGetEpoch (UNSIGNED16 \*pusEpoch); |

Parameters

| pusEpoch (O) | Contains the retrieved current epoch setting. |

Remarks

AdsGetEpoch will retrieve the current value of the default epoch setting for two-digit years. The epoch setting is the same for all connected Advantage servers. See [AdsSetEpoch](ace_adssetepoch.md) for information on the epoch setting.

AdsGetEpoch is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adsgetepochexample)

See Also

[AdsSetEpoch](ace_adssetepoch.md)

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsGetDateFormat](ace_adsgetdateformat.md)
