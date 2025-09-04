AdsBinaryToFile




Advantage Database Server 12  

AdsBinaryToFile/AdsBinaryToFileW

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsBinaryToFile/AdsBinaryToFileW  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsBinaryToFile/AdsBinaryToFileW Advantage Client Engine ace\_Adsbinarytofile Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsBinaryToFile/AdsBinaryToFileW  Advantage Client Engine |  |  |  |  |

Retrieves the binary object from the given field and stores it in the specified file.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsBinaryToFile (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED8 \*pucFileName); |
| UNSIGNED32 | AdsBinaryToFileW (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  WCHAR \*pwcFileName); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve binary object. |
| pucFileName (I) | File in which binary object is to be written. |
| pwcFileName (I) | File in which binary object is to be written. |

Remarks

The file to be written to must be in a path visible to the client. AdsBinaryToFile can resolve DOS or UNC filenames for pucFileName. This function will fail if there is a problem such as running out of disk space on the target device. On a failed function call, the Advantage Client Engine attempts to delete the file it may have created. This behavior could result in an existing file being deleted. For this reason, providing the name of an existing file to store a binary object in is not recommended.

Example

[Click Here](ace_examples.htm#adsbinarytofileexample)

See Also

[AdsFileToBinary](ace_adsfiletobinary.htm)

[AdsGetBinaryLength](ace_adsgetbinarylength.htm)

[AdsGetBinary](ace_adsgetbinary.htm)

[AdsGetFieldType](ace_adsgetfieldtype.htm)