---
title: Ace Adsgetversion
slug: ace_adsgetversion
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetversion.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4041cdbf3939e0a4bc5c1c188cfeb7d263310e84
---

# Ace Adsgetversion

AdsGetVersion

AdsGetVersion

Advantage Client Engine

| AdsGetVersion  Advantage Client Engine |  |  |  |  |

Returns the version of the Advantage Client Engine client driver being used

Syntax

| UNSIGNED32 | AdsGetVersion (UNSIGNED32 \*pulMajor,  UNSIGNED32 \*pulMinor,  UNSIGNED8 \*pucLetter,  UNSIGNED8 \*pucDesc,  UNSIGNED16 \*pusDescLen); |

Parameters

| pulMajor (O) | Returns the major version number. |
| pulMinor (O) | Returns the minor version number (the number after the dot). This version number is a value out of 100. For example, if \*pulMajor is 1, and \*pulMinor is 6, the version is 1.06. If \*pulMajor is 1, and \*pulMinor is 60, the version is 1.60. |
| pucLetter (O) | Returns letter version. This is a single character buffer, not an array. |
| pucDesc (O) | Returns a text description (e.g., "Advantage 32-bit Client Engine for Windows"). |
| pusDescLen (I/O) | On input, this contains the length of pucDesc. On output, it contains the number of characters stored in pucDesc. If the buffer is too short, AE\_INSUFFICIENT\_BUFFER is returned and this argument will contain the necessary length. If the description is not needed, then this value can be specified as zero. |

Remarks

Windows version information is also included in the Advantage Client Engine DLLs. Use Windows Explorer and view the files properties for version information.

Example

[Click Here](ace_examples.md#adsgetversionexample)

See Also

None.
