---
title: Ade Adsgetbinarylength
slug: ade_adsgetbinarylength
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetbinarylength.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 00cddcfdf8d4f40a5a6c14615098c0dbd694f26d
---

# Ade Adsgetbinarylength

AdsGetBinaryLength

TAdsTable.AdsGetBinaryLength

Advantage TDataSet Descendant

| TAdsTable.AdsGetBinaryLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the length of the specified binary object in the given fields of the current record.

Syntax

function AdsGetBinaryLength( strFieldName : String ) : Longint;

Parameter

| strFieldName | Name of the field containing the binary object. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TStream.Size. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetBinaryLength can be used to determine the amount of memory or disk resources needed to manipulate a binary object. Return value is the length of the binary object.

Example

{ note that oStream is a TStream object )

oStream := AdsTable1.CreateBlobStream( FieldByName( LastName, bmReadWrite );

ulBytes := oStream.Size;

See Also

[AdsBinaryToFile](ade_adsbinarytofile.md)

[AdsFileToBinary](ade_adsfiletobinary.md)

[AdsGetBinary](ade_adsgetbinary.md)
