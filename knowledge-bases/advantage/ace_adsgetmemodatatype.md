AdsGetMemoDataType




Advantage Database Server 12  

AdsGetMemoDataType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetMemoDataType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetMemoDataType Advantage Client Engine ace\_Adsgetmemodatatype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetMemoDataType  Advantage Client Engine |  |  |  |  |

Returns the specific type of data stored in a memo field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetMemoDataType (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusType); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of the field to check memo type. |
| pusType (I) | Buffer in which to return the type of memo. This will be one of the following: ADS\_MEMO, ADS\_BINARY, or ADS\_IMAGE. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

AdsGetMemoDataType is provided for compatibility with other Advantage client development environments, which store binary data in DBF memo fields. If a DBF table has a memo field that is used for storing binary data, then this function can be used to determine the exact type of data stored in the memo field on a record-by-record basis. A type of ADS\_IMAGE indicates that an image is stored in the memo field. ADS\_BINARY indicates that some kind of generic binary data is in the field. If the field is a standard memo, the function will return ADS\_MEMO for pusType. ADT tables cannot store binary and image data in standard character memo fields.

Example

[Click Here](ace_examples.htm#adsgetmemodatatypeexample)

See Also

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetString](ace_adsgetstring.htm)

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsGetMemoLength](ace_adsgetmemolength.htm)

[AdsGetBinaryLength](ace_adsgetbinarylength.htm)

[AdsSetBinary](ace_adssetbinary.htm)