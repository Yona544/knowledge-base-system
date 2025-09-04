AdsGetFieldLength




Advantage Database Server 12  

TAdsTable.AdsGetFieldLength

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFieldLength  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFieldLength Advantage TDataSet Descendant ade\_Adsgetfieldlength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFieldLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves length of a field in a table.

Syntax

function AdsGetFieldLength( strFieldName : String ) : Longint;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of field. |

Description

AdsGetFieldLength returns the length of the specified field.  For the Unicode field types ADS\_NCHAR and ADS\_NVARCHAR, the length is returned in characters (the number of 16-bit code units).  For other field types, it returns the number of bytes. For memos, binary fields, and variable-length character fields, this function will return the length of the portion stored in the record rather than the actual data length.

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

[AdsGetBinaryLength](ade_adsgetbinarylength.htm)

[AdsGetFieldDecimals](ade_adsgetfielddecimals.htm)

[AdsGetFieldName](ade_adsgetfieldname.htm)

[AdsGetFieldNum](ade_adsgetfieldnum.htm)

[AdsGetFieldType](ade_adsgetfieldtype.htm)

[AdsGetMemoLength](ade_adsgetmemolength.htm)

[AdsGetNumFields](ade_adsgetnumfields.htm)