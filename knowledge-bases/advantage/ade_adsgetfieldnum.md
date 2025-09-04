AdsGetFieldNum




Advantage Database Server 12  

TAdsTable.AdsGetFieldNum

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFieldNum  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFieldNum Advantage TDataSet Descendant ade\_Adsgetfieldnum Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFieldNum  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the number of a field in a table.

Syntax

function AdsGetFieldNum( strFieldName : String ) : Word;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field. |

Description

The field number is an index in the table of the fields from first to last, with the index of the first field being 1.

Example

AdsTable1.Active := TRUE;

{ retrieve field information }

lFieldLength := AdsTable1.AdsGetFieldLength( 'LastName' );

wFieldDecimals := AdsTable1.AdsGetFieldDecimals( 'LastName' );

lFieldOffset := AdsTable1.AdsGetfieldOffset( 'LastName' );

eFieldType := AdsTable1.AdsGetFieldType( 'LastName' );

wFieldNum := AdsTable1.AdsGetFieldNum( 'LastName' );

{ get the successive field's name }

strFieldName := AdsTable1.AdsGetFieldName( wFieldNum + 1 );

See Also

[AdsGetFieldName](ade_adsgetfieldname.htm)

[AdsGetNumFields](ade_adsgetnumfields.htm)