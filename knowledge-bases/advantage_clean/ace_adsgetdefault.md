---
title: Ace Adsgetdefault
slug: ace_adsgetdefault
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdefault.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 97484ed7717e0304a41f33cc8b8d538dcf949967
---

# Ace Adsgetdefault

AdsGetDefault

AdsGetDefault

Advantage Client Engine

| AdsGetDefault  Advantage Client Engine |  |  |  |  |

Retrieves the current default path

Syntax

| UNSIGNED32 | AdsGetDefault (UNSIGNED8 \*pucDefault,  UNSIGNED16 \*pusLen); |

Parameters

| pucDefault (O) | Return the current default path in this buffer. |
| pusLen (I/O) | Length of buffer on input, length of data stored on output. |

Remarks

AdsGetDefault will return the current default path that has been set by [AdsSetDefault](ace_adssetdefault.md). If no default path has been set, a string of length zero is returned.

AdsGetDefault is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adsgetdefaultexample)

See Also

[AdsSetDefault](ace_adssetdefault.md)

[AdsSetSearchPath](ace_adssetsearchpath.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)
