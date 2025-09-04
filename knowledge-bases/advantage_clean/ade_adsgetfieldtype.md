---
title: Ade Adsgetfieldtype
slug: ade_adsgetfieldtype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfieldtype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1e0e3c76a2a30ad262749d21c6551ad08ccf40e8
---

# Ade Adsgetfieldtype

AdsGetFieldType

TAdsTable.AdsGetFieldType

Advantage TDataSet Descendant

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

[AdsCreateTable](ade_adscreatetable.md)

[AdsGetFieldDecimals](ade_adsgetfielddecimals.md)

[AdsGetFieldName](ade_adsgetfieldname.md)

[AdsGetFieldNum](ade_adsgetfieldnum.md)

[AdsGetFieldOffset](ade_adsgetfieldoffset.md)

[AdsGetMemoDataType](ade_adsgetmemodatatype.md)
