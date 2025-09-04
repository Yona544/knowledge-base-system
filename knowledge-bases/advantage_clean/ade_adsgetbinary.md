---
title: Ade Adsgetbinary
slug: ade_adsgetbinary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetbinary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fdc996f65eb61f65758d70435691eb7639c2d585
---

# Ade Adsgetbinary

AdsGetBinary

TAdsTable.AdsGetBinary

Advantage TDataSet Descendant

| TAdsTable.AdsGetBinary  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the binary data value from the given field.

Syntax

| procedure AdsGetBinary( strFieldName : String; ulOffset : Longint; pucBuf : PChar; var ulBufLen : Longint ); |

Parameter

| strFieldName | Name of field to retrieve. |
| ulOffset | Offset to start reading ( 0 based ) . |
| pucBuf | Return data in this buffer. |
| ulBufLen | Length of given buffer on input, length of returned data on output. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TStream.ReadBuffer. See your Delphi documentation for more information about this native Delphi method.

Description

The data will be retrieved starting at the given offset. The amount of data returned will be the minimum of the ulBufLen and the amount of data available. ulBufLen will be set to the amount of data stored even if there is more data to be returned. Note that this is different from the other routines that return information in buffers because it is expected that blobs can commonly be larger than any allocated buffers. The supported data types are Binary and Image.

To determine the type of data stored in the memo field, use AdsGetMemoDataType. The size of a binary object can be determined by using AdsGetBinaryLength.

Example

{ note that oStream is a TStream object )

oStream := AdsTable1.CreateBlobStream( FieldByName( LastName), bmReadWrite );

oStream.ReadBuffer( buffer, 1000 );

See Also

[AdsBinaryToFile](ade_adsbinarytofile.md)

[AdsFileToBinary](ade_adsfiletobinary.md)

[AdsGetField](ade_adsgetfield.md)

[AdsGetMemoDataType](ade_adsgetmemodatatype.md)

[AdsSetBinary](ade_adssetbinary.md)
