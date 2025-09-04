AdsGetMemoDataType




Advantage Database Server 12  

TAdsTable.AdsGetMemoDataType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetMemoDataType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetMemoDataType Advantage TDataSet Descendant ade\_Adsgetmemodatatype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetMemoDataType  Advantage TDataSet Descendant |  |  |  |  |

Returns the specific type of data stored in a DBF memo field.

Syntax

type TAdsMemoDataTypes = (mdtMEMO, mdtBINARY, mdtIMAGE );

 

function AdsGetMemoDataType( strFieldName : String ) : TAdsMemoDataTypes;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field to check the memo type. |

Description

AdsGetMemoDataType returns the specific type of data stored in a DBF memo field. A type of mdtIMAGE indicates that an image is stored in the DBF memo field. mdtBINARY indicates that some kind of generic binary data is in the DBF memo field. If the DBF field is a standard character memo, the function will return mdtMEMO for pusType. ADT tables cannot store binary and image data in standard character memo fields, so mdtMEMO will always be returned.

Example

AdsTable1.Next;

if ( AdsTable1.AdsGetMemoDataType( 'Notes' ) = mdtMEMO ) then

begin

DBMemo1.DataField := 'Notes';

end;

See Also

[AdsGetBinary](ade_adsgetbinary.htm)

[AdsGetBinaryLength](ade_adsgetbinarylength.htm)

[AdsGetMemoLength](ade_adsgetmemolength.htm)

[AdsGetString](ade_adsgetstring.htm)

[AdsSetBinary](ade_adssetbinary.htm)