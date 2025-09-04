---
title: Ace Adsgetfilter
slug: ace_adsgetfilter
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetfilter.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c6594564a4e98e921eac91f9dc172049b160f9af
---

# Ace Adsgetfilter

AdsGetFilter

AdsGetFilter

Advantage Client Engine

| AdsGetFilter  Advantage Client Engine |  |  |  |  |

Returns the current filter expression for the given table

Syntax

| UNSIGNED32 | AdsGetFilter (ADSHANDLE hTable,  UNSIGNED8 \*pucFilter,  UNSIGNED16 \*pusLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFilter (O) | Return the expression in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Special Return Codes

| AE\_NO\_FILTER | No filter can be cleared or retrieved because no filter was set. |

Remarks

AdsGetFilter will return the current filter expression for the specified table. Note that the case of the expression returned is not guaranteed to be identical to the filter expression that was given in the AdsSetFilter.

Example

[Click Here](ace_examples.md#adsgetfilterexample)

See Also

[AdsSetFilter](ace_adssetfilter.md)

[AdsClearFilter](ace_adsclearfilter.md)
