---
title: Ade Adsgetfielddecimals
slug: ade_adsgetfielddecimals
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfielddecimals.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1b1a351ab374732caf8944f6a1455366989b0032
---

# Ade Adsgetfielddecimals

AdsGetFieldDecimals

TAdsTable.AdsGetFieldDecimals

Advantage TDataSet Descendant

| TAdsTable.AdsGetFieldDecimals  Advantage TDataSet Descendant |  |  |  |  |

Retrieves decimals (for numerics) of a field in a table.

Syntax

function AdsGetFieldDecimals( strFieldName : String ) : Word;

Parameter

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

[AdsGetFieldLength](ade_adsgetfieldlength.md)

[AdsGetFieldName](ade_adsgetfieldname.md)

[AdsGetFieldNum](ade_adsgetfieldnum.md)

[AdsGetFieldType](ade_adsgetfieldtype.md)

[AdsGetNumFields](ade_adsgetnumfields.md)
