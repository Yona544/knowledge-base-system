---
title: Ace Adsgetsearchpath
slug: ace_adsgetsearchpath
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetsearchpath.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 09103ac2cb296678898a75841d427b8cc043e9c9
---

# Ace Adsgetsearchpath

AdsGetSearchPath

AdsGetSearchPath

Advantage Client Engine

| AdsGetSearchPath  Advantage Client Engine |  |  |  |  |

Retrieves the current search path

Syntax

| UNSIGNED32 | AdsGetSearchPath (UNSIGNED8 \*pucPath,  UNSIGNED16 \*pusLen); |

Parameters

| pucPath (O) | Return the search path in this buffer. |
| pusLen (I/O) | Length of buffer on input, length of search path on output. |

Remarks

AdsGetSearchPath retrieves the current search path in the supplied buffer. If the search path has not been set, a string of length zero is returned.

AdsGetSearchPath is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adsgetsearchpathexample)

See Also

[AdsSetSearchPath](ace_adssetsearchpath.md)

[AdsSetDefault](ace_adssetdefault.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)
