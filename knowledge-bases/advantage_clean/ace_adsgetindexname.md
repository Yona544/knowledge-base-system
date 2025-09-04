---
title: Ace Adsgetindexname
slug: ace_adsgetindexname
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexname.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c4a36e201499dec35a591a990c5c18d962142162
---

# Ace Adsgetindexname

AdsGetIndexName

AdsGetIndexName

Advantage Client Engine

| AdsGetIndexName  Advantage Client Engine |  |  |  |  |

Retrieves the name of the index order.

Syntax

| UNSIGNED32 | AdsGetIndexName (ADSHANDLE hIndex,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pucName (O) | Return the name in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. If it is the handle of a tag from a compound index file, the tag name is returned. Otherwise the base filename of the NTX or IDX is returned. |

Remarks

For NTX and IDX files, this function will return the base of the filename (up to 8 characters). For CDX indexes, this function will return the tag name (up to 10 characters). For ADI indexes, this function will return the tag name (up to 128 characters).

Example

[Click Here](ace_examples.md#adsgetindexnameexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsGetIndexHandle](ace_adsgetindexhandle.md)

[AdsGetIndexFilename](ace_adsgetindexfilename.md)
