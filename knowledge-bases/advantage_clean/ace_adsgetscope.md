---
title: Ace Adsgetscope
slug: ace_adsgetscope
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetscope.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9fe14fd75e0b0f4baac0fdb03d4659d041e60f96
---

# Ace Adsgetscope

AdsGetScope

AdsGetScope

Advantage Client Engine

| AdsGetScope  Advantage Client Engine |  |  |  |  |

Retrieves the specified scope from the given index order.

Syntax

| UNSIGNED32 | AdsGetScope (ADSHANDLE hIndex,  UNSIGNED16 usScopeOption,  UNSIGNED8 \*pucScope,  UNSIGNED16 \*pusBufLen); |

Parameters

| hIndex (I) | Handle of index order. |
| usScopeOption (I) | Indicates which scope value to retrieve. Options are ADS\_TOP, ADS\_BOTTOM. |
| pucScope (O) | Return the specified scope in this buffer. |
| pusBufLen (I/O) | Length of given buffer on input, length of returned data on output. |

Special Return Codes

| AE\_NO\_SCOPE | No scope was set, so a scope cannot be returned or cleared. |

Remarks

AdsGetScope returns the indicated scope setting in the form of an index key. The value sent in a call to [AdsSetScope](ace_adssetscope.md) was converted to a valid index key by the Advantage Client Engine. It may be necessary to convert the key to another form to make it useful. For example, when an application sets a scope on a date index, the Advantage Client Engine converts the date value to match the key data type. For a CDX and ADI indexes, this would be an 8-byte Julian date representation.

Example

[Click Here](ace_examples.md#adsgetscopeexample)

See Also

[AdsClearScope](ace_adsclearscope.md)

[AdsSetScope](ace_adssetscope.md)
