AdsBinaryToFile




Advantage Database Server 12  

TAdsTable.AdsBinaryToFile

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsBinaryToFile  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsBinaryToFile Advantage TDataSet Descendant ade\_Adsbinarytofile Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsBinaryToFile  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the binary object from the given field and stores it in the specified file.

Syntax

procedure AdsBinaryToFile( strFieldName, strFileName : String );

Parameters

|  |  |
| --- | --- |
| strFieldName | Binary field name from a table. |
| strFileName | File name to store the binary object. |

CATUION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi methods to use instead are: TDataSet.CreateBlobStream, TFileStream.Create, TStream.CopyFrom. See your Delphi documentation for more information about these native Delphi methods.

Description

The file to be written to must be in a path visible to the client. AdsBinaryToFile can resolve DOS or UNC filenames for strFileName. This function will fail if there is a problem such as running out of disk space on the target device. On a failed function call, the Advantage Client Engine attempts to delete the file it may have created. This behavior could result in an existing file being deleted. Providing the name of an existing file to store a binary object in is not recommended.

You can use AdsBinaryToFile with the field type Binary and Image only.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.AdsBinaryToFile( Picture, c:\temp\image.jpg );

See Also

[AdsFileToBinary](ade_adsfiletobinary.htm)

[AdsGetBinary](ade_adsgetbinary.htm)

[AdsGetBinaryLength](ade_adsgetbinarylength.htm)