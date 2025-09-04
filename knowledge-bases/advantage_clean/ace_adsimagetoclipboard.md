---
title: Ace Adsimagetoclipboard
slug: ace_adsimagetoclipboard
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsimagetoclipboard.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a810a06fc316a40110893307397b7886cabcc255
---

# Ace Adsimagetoclipboard

AdsImageToClipboard

AdsImageToClipboard

Advantage Client Engine

| AdsImageToClipboard  Advantage Client Engine |  |  |  |  |

Copies an image from a binary field onto the Windows clipboard

Syntax

| UNSIGNED32 | AdsImageToClipboard (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field image is stored in. |

Remarks

Copies the image stored in the indicated field in the current record onto the Windows clipboard. The image is then available for clipboard operations such as pasting into other Windows applications. The image remains available until either another object is copied to the clipboard or the clipboard is cleared.

Note This API only works on valid BMP images.

 

Note This API only works on ADS\_IMAGE fields.

Example

None

See Also

[AdsGetBinary](ace_adsgetbinary.md)

[AdsSetBinary](ace_adssetbinary.md)

[AdsGetFieldType](ace_adsgetfieldtype.md)

[AdsGetMemoDataType](ace_adsgetmemodatatype.md)
