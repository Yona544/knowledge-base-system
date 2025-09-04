---
title: Ace Adsgetlasttableupdate
slug: ace_adsgetlasttableupdate
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetlasttableupdate.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: dda3169f85d59f0ab63a2ea5acc0e92a87de2b10
---

# Ace Adsgetlasttableupdate

AdsGetLastTableUpdate

AdsGetLastTableUpdate

Advantage Client Engine

| AdsGetLastTableUpdate  Advantage Client Engine |  |  |  |  |

Returns the date the table was last updated.

Syntax

| UNSIGNED32 | AdsGetLastTableUpdate (ADSHANDLE hTable,  UNSIGNED8 \*pucDate,  UNSIGNED16\*pusDateLen); |

Parameters

| hTable (I) | Handle of a table or cursor. |
| pucDate (O) | Day the table was last updated. |
| pusDateLen (I/O) | On input, the length of the pucDate buffer. On output, the length of the returned data. |

Remarks

The date returned is the day the table was last written to, and formatted according to the current date format.

Example

None.

See Also

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsGetEpoch](ace_adsgetepoch.md)

[AdsOpenTable](ace_adsopentable.md)
