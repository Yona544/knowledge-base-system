---
title: Ace Adsisfound
slug: ace_adsisfound
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisfound.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 83d90642915e4e6db33f6698c89ccc9aca9043c6
---

# Ace Adsisfound

AdsIsFound

AdsIsFound

Advantage Client Engine

| AdsIsFound  Advantage Client Engine |  |  |  |  |

Returns True if the last seek or locate function call was successful

Syntax

| UNSIGNED32 | AdsIsFound (ADSHANDLE hTable,  UNSIGNED16 \*pbFound); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pbFound (O) | Return True if record found. |

Remarks

The found flag will not remain set after other movement in a table. Therefore, it is only guaranteed to be valid immediately following a call to AdsSeek, AdsLocate, or AdsContinue.

Example

[Click Here](ace_examples.md#adsisfoundexample)

See Also

[AdsSeek](ace_adsseek.md)

[AdsLocate](ace_adslocate.md)

[AdsContinue](ace_adscontinue.md)
