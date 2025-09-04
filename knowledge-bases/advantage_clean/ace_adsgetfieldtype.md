---
title: Ace Adsgetfieldtype
slug: ace_adsgetfieldtype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetfieldtype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4b3c0ca0e8cfadfe8700186ada2d3acf2c5ad47b
---

# Ace Adsgetfieldtype

AdsGetFieldType

AdsGetFieldType

Advantage Client Engine

| AdsGetFieldType  Advantage Client Engine |  |  |  |  |

Retrieves the type of a field in a table

Syntax

| UNSIGNED32 | AdsGetFieldType (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusType); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field. |
| pusType (O) | Retrieves the type of the field (ADS\_LOGICAL, ADS\_NUMERIC, ADS\_DATE, ADS\_STRING, ADS\_CISTRING, ADS\_MEMO, ADS\_VARCHAR, ADS\_COMPACTDATE, ADS\_DOUBLE, ADS\_INTEGER, ADS\_IMAGE, ADS\_BINARY; ADS\_SHORTINT; ADS\_TIME; ADS\_TIMESTAMP; ADS\_AUTOINC; ADS\_RAW; ADS\_CURDOUBLE, ADS\_MONEY, ADS\_ROWVERSION, ADS\_MODTIME) |

Remarks

For compatibility with other Advantage client development environments, memo fields can be used to store image and binary data in DBF tables. ADT tables cannot store image or binary data in character memo fields. If your DBF table has memo fields with binary data in them, you can use [AdsGetMemoDataType](ace_adsgetmemodatatype.md) to determine the exact data type when AdsGetFieldType returns ADS\_MEMO.

Example

[Click Here](ace_examples.md#adsgetfieldtypeexample)

See Also

[AdsGetFieldName](ace_adsgetfieldname.md)

[AdsGetFieldNum](ace_adsgetfieldnum.md)

[AdsGetFieldOffset](ace_adsgetfieldoffset.md)

[AdsGetFieldDecimals](ace_adsgetfielddecimals.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetMemoDataType](ace_adsgetmemodatatype.md)
