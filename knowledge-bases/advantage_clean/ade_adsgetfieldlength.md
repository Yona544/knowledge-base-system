---
title: Ade Adsgetfieldlength
slug: ade_adsgetfieldlength
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfieldlength.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3989843a70673063972917f8e541ff2a9df9e53e
---

# Ade Adsgetfieldlength

AdsGetFieldLength

TAdsTable.AdsGetFieldLength

Advantage TDataSet Descendant

| TAdsTable.AdsGetFieldLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves length of a field in a table.

Syntax

function AdsGetFieldLength( strFieldName : String ) : Longint;

Parameter

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

[AdsGetBinaryLength](ade_adsgetbinarylength.md)

[AdsGetFieldDecimals](ade_adsgetfielddecimals.md)

[AdsGetFieldName](ade_adsgetfieldname.md)

[AdsGetFieldNum](ade_adsgetfieldnum.md)

[AdsGetFieldType](ade_adsgetfieldtype.md)

[AdsGetMemoLength](ade_adsgetmemolength.md)

[AdsGetNumFields](ade_adsgetnumfields.md)
