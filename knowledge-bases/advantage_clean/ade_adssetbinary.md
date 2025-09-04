---
title: Ade Adssetbinary
slug: ade_adssetbinary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetbinary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d9253a17daeffe71918465773a8d1c5dd1dedc02
---

# Ade Adssetbinary

AdsSetBinary

TAdsTable.AdsSetBinary

Advantage TDataSet Descendant

| TAdsTable.AdsSetBinary  Advantage TDataSet Descendant |  |  |  |  |

Stores given data as a blob in the given field.

Syntax

type TAdsBinaryTypes = ( btBINARY, btIMAGE );

 

procedure AdsSetBinary( strFieldName : String; eBinaryType : TAdsBinaryTypes; ulTotalLength : Longint; ulOffset : Longint; pucBuf : PChar; ulBufLength : Longint );

Parameter

| strFieldName | Name of field to set. |
| eBinaryType | Indicates type of binary data. Values are btBINARY and btIMAGE. |
| ulTotalLength | Total length of data being stored. If the data is being stored with a single call, then this parameter should be the same as ulBufLen. If the data is being stored with multiple calls, then this parameter should be the same for each call and must represent the total length of the binary date. |
| ulOffset | Offset to which to start writing. |
| pucBuf | Store this data in the field. |
| ulBufLength | Length of data in the buffer for this call. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TStream.WriteBuffer. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetBinary sets binary objects that are held in memory. For larger binary objects, AdsFileToBinary is provided. Be sure to specify btIMAGE if storing an image in the field. After storing the data, use AdsGetMemoDataType to determine the type of data stored in a memo field.

Note Use of this function is illegal in a transaction if the entire binary value is not being stored to the Binary/Image field in a single call. In other words, if the value in the ulTotalLength parameter is not the same as the value in the ulBufLength parameter, use of this function is illegal in a transaction. If the entire binary value is sent in a single call to AdsSetBinary, use of this function is supported in a transaction.

Example

{ note that oStream is a TStream object )

oStream := AdsTable1.CreateBlobStream( AdsTable1 FieldByName( LastName), bmReadWrite );

oStream.WriteBuffer( buffer, 1000 );

See Also

[AdsFileToBinary](ade_adsfiletobinary.md)

[AdsGetBinary](ade_adsgetbinary.md)

[AdsGetBinaryLength](ade_adsgetbinarylength.md)

[AdsGetMemoDataType](ade_adsgetmemodatatype.md)

[AdsSetField](ade_adssetfield.md)
