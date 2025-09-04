AdsGetMemoLength




Advantage Database Server 12  

AdsGetMemoLength

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetMemoLength  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetMemoLength Advantage Client Engine ace\_Adsgetmemolength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetMemoLength  Advantage Client Engine |  |  |  |  |

Retrieves the length of the specified memo field of the current record.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetMemoLength (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 \*pulLength); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of memo field. |
| pulLength (O) | Return length of memo. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

AdsGetMemoLength returns the length of the specified memo field in characters.  For Unicode memo fields of type ADS\_NMEMO this is the number of 16-bit code units.  For memo fields of type ADS\_MEMO, the length in characters is the same as the length in bytes. AdsGetMemoLength will not support binary object fields. Use [AdsGetBinaryLength](ace_adsgetbinarylength.htm) for binary fields.

Example

[Click Here](ace_examples.htm#adsgetmemolengthexample)

See Also

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetFieldLength](ace_adsgetfieldlength.htm)

[AdsGetString](ace_adsgetstring.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsGetMemoDataType](ace_adsgetmemodatatype.htm)