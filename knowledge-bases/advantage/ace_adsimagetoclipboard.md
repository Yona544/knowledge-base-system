AdsImageToClipboard




Advantage Database Server 12  

AdsImageToClipboard

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsImageToClipboard  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsImageToClipboard Advantage Client Engine ace\_Adsimagetoclipboard Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsImageToClipboard  Advantage Client Engine |  |  |  |  |

Copies an image from a binary field onto the Windows clipboard

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsImageToClipboard (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field image is stored in. |

Remarks

Copies the image stored in the indicated field in the current record onto the Windows clipboard. The image is then available for clipboard operations such as pasting into other Windows applications. The image remains available until either another object is copied to the clipboard or the clipboard is cleared.

Note This API only works on valid BMP images.

 

Note This API only works on ADS\_IMAGE fields.

Example

None

See Also

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsSetBinary](ace_adssetbinary.htm)

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetMemoDataType](ace_adsgetmemodatatype.htm)