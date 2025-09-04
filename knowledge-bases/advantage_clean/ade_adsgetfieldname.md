---
title: Ade Adsgetfieldname
slug: ade_adsgetfieldname
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfieldname.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2db77d2a228977caa4c19adbd65353cce69139fc
---

# Ade Adsgetfieldname

AdsGetFieldName

TAdsTable.AdsGetFieldName

Advantage TDataSet Descendant

| TAdsTable.AdsGetFieldName  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the name of a field in a table.

Syntax

function AdsGetFieldName( usFieldNum : Word ) : String;

Parameter

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

[AdsGetFieldNum](ade_adsgetfieldnum.md)

[AdsGetNumFields](ade_adsgetnumfields.md)
