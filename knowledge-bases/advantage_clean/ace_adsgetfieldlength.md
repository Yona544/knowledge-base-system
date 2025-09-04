---
title: Ace Adsgetfieldlength
slug: ace_adsgetfieldlength
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetfieldlength.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e188d571e0fc9de3140c8a1dd171e522f934a7bc
---

# Ace Adsgetfieldlength

AdsGetFieldLength

AdsGetFieldLength / AdsGetFieldLength100

Advantage Client Engine

| AdsGetFieldLength / AdsGetFieldLength100  Advantage Client Engine |  |  |  |  |

Retrieves the length of a field in a table

Syntax

| UNSIGNED32 | AdsGetFieldLength ( ADSHANDLE hTable,                     UNSIGNED8 \*pucFldName,                     UNSIGNED32 \*pulLength); |
| UNSIGNED32 | AdsGetFieldLength100( ADSHANDLE hTable,                       UNSIGNED8 \*pucFldName,                       UNSIGNED32 ulOptions,                       UNSIGNED32 \*pulLength ); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pulLength (O) | Return field length. |
| ulOptions (I) | Bit fields options to determine which length to return. The available options are:    ADS\_BYTE\_LENGTH: return the length of field in number of bytes. The returned length is the size available for storing data.    ADS\_CODEUNIT\_LENGTH: return the length of the field in number of code units or characters. This is the default option. The length returned with this option is only meaningful for NCHAR and NVARCHAR field type. The length returned is the number of characters can be stored in the field. For other field types, this option returns the same length as the ADS\_BYTE\_LENGTH option.    ADS\_BYTE\_LENGTH\_IN\_BUFFER: return the length of the field in the record buffer. Some field types reserve additional bytes in the records buffer for house keeping. For those field types, the ADS\_BYTE\_LENGTH\_IN\_BUFFER will be different from ADS\_BYTE\_LENGTH. |

Remarks

AdsGetFieldLength returns the length of the specified field.  For the Unicode field types ADS\_NCHAR and ADS\_NVARCHAR, the length is returned in characters (the number of 16-bit code units).  For other field types, it returns the number of bytes. For memos, binary fields, and variable length character fields, this function will return the length of the portion stored in the record rather than the actual data length.

AdsGetFieldLength100 provides the option to return the length in number of code units or characters for all Unicode character field types except the NMEMO field type.

Example

[Click Here](ace_examples.md#adsgetfieldlengthexample)

See Also

[AdsGetFieldDecimals](ace_adsgetfielddecimals.md)

[AdsGetFieldName](ace_adsgetfieldname.md)

[AdsGetFieldNum](ace_adsgetfieldnum.md)

[AdsGetNumFields](ace_adsgetnumfields.md)

[AdsGetBinaryLength](ace_adsgetbinarylength.md)

[AdsGetMemoLength](ace_adsgetmemolength.md)

[AdsGetFieldType](ace_adsgetfieldtype.md)
