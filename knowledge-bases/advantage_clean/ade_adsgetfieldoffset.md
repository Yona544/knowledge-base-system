---
title: Ade Adsgetfieldoffset
slug: ade_adsgetfieldoffset
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfieldoffset.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a08867e83b6ca84ae1a63a33d124da39e51d7b83
---

# Ade Adsgetfieldoffset

AdsGetFieldOffset

TAdsTable.AdsGetFieldOffset

Advantage TDataSet Descendant

| TAdsTable.AdsGetFieldOffset  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the offset of a field in a table.

Syntax

function AdsGetFieldOffset( strFieldName : String ) : Longint;

Parameter

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

[AdsGetFieldLength](ade_adsgetfieldlength.md)

[AdsGetFieldName](ade_adsgetfieldname.md)

[AdsGetFieldNum](ade_adsgetfieldnum.md)

[AdsGetNumFields](ade_adsgetnumfields.md)
