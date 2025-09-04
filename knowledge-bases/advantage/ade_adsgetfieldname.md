AdsGetFieldName




Advantage Database Server 12  

TAdsTable.AdsGetFieldName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFieldName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFieldName Advantage TDataSet Descendant ade\_Adsgetfieldname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFieldName  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the name of a field in a table.

Syntax

function AdsGetFieldName( usFieldNum : Word ) : String;

Parameter

|  |  |
| --- | --- |
| usFieldNum | Field position of interest (the first field is 1). |

Description

Retrieves the name of a field in a table. For ADT tables, valid field names are 128 characters or less and can contain any character value except 0 (NULL), ";" (a semi-colon), or "," (a comma). For DBF tables, valid field names are 10 characters or less. Valid characters for field names are the letters a-z and A-Z, digits 0-9, and the underscore "\_" character.

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

[AdsGetFieldNum](ade_adsgetfieldnum.htm)

[AdsGetNumFields](ade_adsgetnumfields.htm)