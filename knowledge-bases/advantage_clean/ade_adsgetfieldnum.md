---
title: Ade Adsgetfieldnum
slug: ade_adsgetfieldnum
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfieldnum.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 364c08ce065495c9ecf92d458f51819c7c82f031
---

# Ade Adsgetfieldnum

AdsGetFieldNum

TAdsTable.AdsGetFieldNum

Advantage TDataSet Descendant

| TAdsTable.AdsGetFieldNum  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the number of a field in a table.

Syntax

function AdsGetFieldNum( strFieldName : String ) : Word;

Parameter

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

[AdsGetFieldName](ade_adsgetfieldname.md)

[AdsGetNumFields](ade_adsgetnumfields.md)
