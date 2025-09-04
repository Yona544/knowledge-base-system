---
title: Ace Adsfiletobinary
slug: ace_adsfiletobinary
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfiletobinary.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7fd0ad53085f5da102ce845919c7e15cdd69b505
---

# Ace Adsfiletobinary

AdsFileToBinary

AdsFileToBinary/AdsFileToBinaryW

Advantage Client Engine

| AdsFileToBinary/AdsFileToBinaryW  Advantage Client Engine |  |  |  |  |

Stores the contents of the given file as a binary object in the specified field.

Syntax

| UNSIGNED32 | AdsFileToBinary (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 usBinaryType,  UNSIGNED8 \*pucFileName); |
| UNSIGNED32 | AdsFileToBinaryW (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 usBinaryType,  WCHAR \*pwcFileName); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to update. |
| usBinaryType (I) | Indicates type of binary data. Values are ADS\_IMAGE and ADS\_BINARY. |
| pucFileName (I) | File from which to retrieve the binary object. |
| pwcFileName (I) | File from which to retrieve the binary object. |

Remarks

The file to be opened must be in a path visible to the client. AdsFileToBinary can resolve DOS or UNC filenames for pucFileName. The binary object is copied in fragments that are as large as both the Advantage Database Server and underlying networks can accommodate.

This API can be used to store binary data in memo fields. If used this way, [AdsGetMemoDataType](ace_adsgetmemodatatype.md) can be called to determine the type of data stored in the memo field.

Example

[Click Here](ace_examples.md#adsfiletobinaryexample)

See Also

[AdsGetBinaryLength](ace_adsgetbinarylength.md)

[AdsGetBinary](ace_adsgetbinary.md)

[AdsBinaryToFile](ace_adsbinarytofile.md)

[AdsSetBinary](ace_adssetbinary.md)

[AdsGetFieldType](ace_adsgetfieldtype.md)

[AdsGetMemoDataType](ace_adsgetmemodatatype.md)
