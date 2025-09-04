AdsGetBinaryLength




Advantage Database Server 12  

AdsGetBinaryLength

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetBinaryLength  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetBinaryLength Advantage Client Engine ace\_Adsgetbinarylength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetBinaryLength  Advantage Client Engine |  |  |  |  |

Retrieves the length of the specified binary object in the given fields of the current record.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetBinaryLength (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 \*pulLength); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field containing the binary object. |
| pulLength (O) | Return length of binary object. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF. |

Remarks

AdsGetBinaryLength can be used to determine the amount of memory or disk resources needed to manipulate a binary object.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.htm#adsgetbinarylengthexample)

See Also

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsFileToBinary](ace_adsfiletobinary.htm)

[AdsBinaryToFile](ace_adsbinarytofile.htm)