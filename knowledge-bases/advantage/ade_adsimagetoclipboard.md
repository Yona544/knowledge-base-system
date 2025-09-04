AdsImageToClipboard




Advantage Database Server 12  

TAdsTable.AdsImageToClipboard

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsImageToClipboard  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsImageToClipboard Advantage TDataSet Descendant ade\_Adsimagetoclipboard Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsImageToClipboard  Advantage TDataSet Descendant |  |  |  |  |

Copies an image from a binary field onto the Windows clipboard.

Syntax

procedure AdsImageToClipboard( strFldName : String );

Parameter

|  |  |
| --- | --- |
| strFldName | Name of field image is stored in. |

Description

Copies the image stored in the indicated field in the current record onto the Windows clipboard. The image is then available for clipboard operations such as pasting into other Windows applications. The image remains available until either another object is copied to the clipboard or the clipboard is cleared.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.AdsImageToClipboard( Picture );

See Also

[AdsGetBinary](ade_adsgetbinary.htm)

[AdsGetMemoDataType](ade_adsgetmemodatatype.htm)

[AdsSetBinary](ade_adssetbinary.htm)