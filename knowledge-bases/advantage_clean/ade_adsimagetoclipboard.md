---
title: Ade Adsimagetoclipboard
slug: ade_adsimagetoclipboard
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsimagetoclipboard.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0c77ed0a4b4db5b94c76ef20bebdda2614eef6cb
---

# Ade Adsimagetoclipboard

AdsImageToClipboard

TAdsTable.AdsImageToClipboard

Advantage TDataSet Descendant

| TAdsTable.AdsImageToClipboard  Advantage TDataSet Descendant |  |  |  |  |

Copies an image from a binary field onto the Windows clipboard.

Syntax

procedure AdsImageToClipboard( strFldName : String );

Parameter

| strFldName | Name of field image is stored in. |

Description

Copies the image stored in the indicated field in the current record onto the Windows clipboard. The image is then available for clipboard operations such as pasting into other Windows applications. The image remains available until either another object is copied to the clipboard or the clipboard is cleared.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.AdsImageToClipboard( Picture );

See Also

[AdsGetBinary](ade_adsgetbinary.md)

[AdsGetMemoDataType](ade_adsgetmemodatatype.md)

[AdsSetBinary](ade_adssetbinary.md)
