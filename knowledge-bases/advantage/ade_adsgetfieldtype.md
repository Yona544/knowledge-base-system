AdsGetFieldType




Advantage Database Server 12  

TAdsTable.AdsGetFieldType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetFieldType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetFieldType Advantage TDataSet Descendant ade\_Adsgetfieldtype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetFieldType  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the type of a field in a table.

Syntax

TAdsFieldTypes = ( AdsfldLOGICAL, AdsfldNUMERIC, AdsfldDATE, AdsfldSTRING,

AdsfldCISTRING, AdsfldMEMO, AdsfldVARCHAR,

AdsfldCOMPACTDATE, AdsfldDOUBLE, AdsfldINTEGER,

AdsfldSHORTINT, AdsfldTIME, AdsfldTIMESTAMP,

AdsfldAUTOINC, AdsfldRAW, AdsfldCURDOUBLE, AdsfldMONEY );

 

function AdsGetFieldType( strFieldName : String ) : TAdsFieldTypes;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of the Field. |

Description

The return is the type of the field. If the field type returned is mdtMEMO, the field may actually be type mdtBINARY or mdtIMAGE. The exact type can be determined by calling AdsGetMemoDataType.

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

[AdsCreateTable](ade_adscreatetable.htm)

[AdsGetFieldDecimals](ade_adsgetfielddecimals.htm)

[AdsGetFieldName](ade_adsgetfieldname.htm)

[AdsGetFieldNum](ade_adsgetfieldnum.htm)

[AdsGetFieldOffset](ade_adsgetfieldoffset.htm)

[AdsGetMemoDataType](ade_adsgetmemodatatype.htm)