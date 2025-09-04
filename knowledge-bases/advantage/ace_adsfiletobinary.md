AdsFileToBinary




Advantage Database Server 12  

AdsFileToBinary/AdsFileToBinaryW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFileToBinary/AdsFileToBinaryW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFileToBinary/AdsFileToBinaryW Advantage Client Engine ace\_Adsfiletobinary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFileToBinary/AdsFileToBinaryW  Advantage Client Engine |  |  |  |  |

Stores the contents of the given file as a binary object in the specified field.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsFileToBinary (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 usBinaryType,  UNSIGNED8 \*pucFileName); |
| UNSIGNED32 | AdsFileToBinaryW (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 usBinaryType,  WCHAR \*pwcFileName); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to update. |
| usBinaryType (I) | Indicates type of binary data. Values are ADS\_IMAGE and ADS\_BINARY. |
| pucFileName (I) | File from which to retrieve the binary object. |
| pwcFileName (I) | File from which to retrieve the binary object. |

Remarks

The file to be opened must be in a path visible to the client. AdsFileToBinary can resolve DOS or UNC filenames for pucFileName. The binary object is copied in fragments that are as large as both the Advantage Database Server and underlying networks can accommodate.

This API can be used to store binary data in memo fields. If used this way, [AdsGetMemoDataType](ace_adsgetmemodatatype.htm) can be called to determine the type of data stored in the memo field.

Example

[Click Here](ace_examples.htm#adsfiletobinaryexample)

See Also

[AdsGetBinaryLength](ace_adsgetbinarylength.htm)

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsBinaryToFile](ace_adsbinarytofile.htm)

[AdsSetBinary](ace_adssetbinary.htm)

[AdsGetFieldType](ace_adsgetfieldtype.htm)

[AdsGetMemoDataType](ace_adsgetmemodatatype.htm)