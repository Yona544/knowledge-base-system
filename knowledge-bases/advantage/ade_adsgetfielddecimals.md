AdsGetFieldDecimals




Advantage Database Server 12  

TAdsTable.AdsGetFieldDecimals

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFieldDecimals  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFieldDecimals Advantage TDataSet Descendant ade\_Adsgetfielddecimals Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFieldDecimals  Advantage TDataSet Descendant |  |  |  |  |

Retrieves decimals (for numerics) of a field in a table.

Syntax

function AdsGetFieldDecimals( strFieldName : String ) : Word;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the field. |

Description

AdsGetFieldDecimals returns the number of digits of decimal precision in the field to the right of the decimal point in a numeric field.

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

[AdsGetFieldType](ade_adsgetfieldtype.htm)

[AdsGetNumFields](ade_adsgetnumfields.htm)