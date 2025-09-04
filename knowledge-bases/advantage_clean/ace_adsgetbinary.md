---
title: Ace Adsgetbinary
slug: ace_adsgetbinary
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetbinary.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fbec79d4bbc2a77a44d4db3e8763b3c7ef11ecde
---

# Ace Adsgetbinary

AdsGetBinary

AdsGetBinary

Advantage Client Engine

| AdsGetBinary  Advantage Client Engine |  |  |  |  |

Retrieves the binary data value from the given field.

Syntax

| UNSIGNED32 | AdsGetBinary (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 ulOffset,  UNSIGNED8 \*pucBuf,  UNSIGNED32 \*pulLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| ulOffset (I) | Offset to start reading (0 based). |
| pucBuf (O) | Return data in this buffer. |
| pulLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

The data will be retrieved starting at the given offset. The amount of data returned will be the minimum of the pulLen and the amount of data available. The parameter pulLen will be set to the amount of data stored even if there is more data to be returned. This is different from the other routines that return information in buffers because it is expected that BLOBs can commonly be larger than any allocated buffers. The supported data types are Binary and Image.

The size of a binary object can be determined by using [AdsGetBinaryLength](ace_adsgetbinarylength.md).

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetbinaryexample)

See Also

[AdsGetField](ace_adsgetfield.md)

[AdsSetBinary](ace_adssetbinary.md)

[AdsBinaryToFile](ace_adsbinarytofile.md)

[AdsFileToBinary](ace_adsfiletobinary.md)

[AdsGetFieldType](ace_adsgetfieldtype.md)

[AdsGetMemoDataType](ace_adsgetmemodatatype.md)
