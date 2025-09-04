AdsGetFieldOffset




Advantage Database Server 12  

TAdsTable.AdsGetFieldOffset

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFieldOffset  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFieldOffset Advantage TDataSet Descendant ade\_Adsgetfieldoffset Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFieldOffset  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the offset of a field in a table.

Syntax

function AdsGetFieldOffset( strFieldName : String ) : Longint;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the Field. |

Description

Returns the offset of the field in the tables record image.

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

[AdsGetFieldLength](ade_adsgetfieldlength.htm)

[AdsGetFieldName](ade_adsgetfieldname.htm)

[AdsGetFieldNum](ade_adsgetfieldnum.htm)

[AdsGetNumFields](ade_adsgetnumfields.htm)