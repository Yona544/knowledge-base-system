---
title: Ade Adsfiletobinary
slug: ade_adsfiletobinary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsfiletobinary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 77fd1e6aa7dc195eb22b9f71ababae792839abb6
---

# Ade Adsfiletobinary

AdsFileToBinary

TAdsTable.AdsFileToBinary

Advantage TDataSet Descendant

| TAdsTable.AdsFileToBinary  Advantage TDataSet Descendant |  |  |  |  |

Stores the contents of the given file as a binary object in the specified field.

Syntax

type TAdsBinaryTypes = ( btBINARY, btIMAGE );

 

procedure AdsFileToBinary( strFieldName : String; eBinaryType : TAdsBinaryTypes; strFileName : String );

Parameter

| strFieldName | Name of the field to update. |
| eBinaryType | Indicates the type of binary data. |
| strFileName | File from which to retrieve the binary object. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi methods to use instead are: TDataSet.CreateBlobStream, TFileStream.Create, TStream.CopyFrom. See your Delphi documentation for more information about these native Delphi methods.

Description

The file to be opened must be in a path visible to the client. AdsFileToBinary can resolve DOS or UNC filenames for pucFileName. The binary object is copied in fragments that are as large as the Advantage Database Server and underlying networks can accommodate.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.AdsFileToBinary( 'Picture', btImage, 'c:\temp\image.jpg' );

 

See Also

[AdsBinaryToFile](ade_adsbinarytofile.md)

[AdsGetBinary](ade_adsgetbinary.md)

[AdsGetBinaryLength](ade_adsgetbinarylength.md)

[AdsSetBinary](ade_adssetbinary.md)
