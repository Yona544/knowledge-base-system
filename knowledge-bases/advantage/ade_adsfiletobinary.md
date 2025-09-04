AdsFileToBinary




Advantage Database Server 12  

TAdsTable.AdsFileToBinary

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsFileToBinary  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsFileToBinary Advantage TDataSet Descendant ade\_Adsfiletobinary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsFileToBinary  Advantage TDataSet Descendant |  |  |  |  |

Stores the contents of the given file as a binary object in the specified field.

Syntax

type TAdsBinaryTypes = ( btBINARY, btIMAGE );

 

procedure AdsFileToBinary( strFieldName : String; eBinaryType : TAdsBinaryTypes; strFileName : String );

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to update. |
| eBinaryType | Indicates the type of binary data. |
| strFileName | File from which to retrieve the binary object. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi methods to use instead are: TDataSet.CreateBlobStream, TFileStream.Create, TStream.CopyFrom. See your Delphi documentation for more information about these native Delphi methods.

Description

The file to be opened must be in a path visible to the client. AdsFileToBinary can resolve DOS or UNC filenames for pucFileName. The binary object is copied in fragments that are as large as the Advantage Database Server and underlying networks can accommodate.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.AdsFileToBinary( 'Picture', btImage, 'c:\temp\image.jpg' );

 

See Also

[AdsBinaryToFile](ade_adsbinarytofile.htm)

[AdsGetBinary](ade_adsgetbinary.htm)

[AdsGetBinaryLength](ade_adsgetbinarylength.htm)

[AdsSetBinary](ade_adssetbinary.htm)