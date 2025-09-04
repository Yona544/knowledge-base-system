AdsGetBinaryLength




Advantage Database Server 12  

TAdsTable.AdsGetBinaryLength

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetBinaryLength  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetBinaryLength Advantage TDataSet Descendant ade\_Adsgetbinarylength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetBinaryLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the length of the specified binary object in the given fields of the current record.

Syntax

function AdsGetBinaryLength( strFieldName : String ) : Longint;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field containing the binary object. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TStream.Size. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetBinaryLength can be used to determine the amount of memory or disk resources needed to manipulate a binary object. Return value is the length of the binary object.

Example

{ note that oStream is a TStream object )

oStream := AdsTable1.CreateBlobStream( FieldByName( LastName, bmReadWrite );

ulBytes := oStream.Size;

See Also

[AdsBinaryToFile](ade_adsbinarytofile.htm)

[AdsFileToBinary](ade_adsfiletobinary.htm)

[AdsGetBinary](ade_adsgetbinary.htm)