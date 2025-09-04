---
title: Ace Adsgetmemodatatype
slug: ace_adsgetmemodatatype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetmemodatatype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2721285825f25a423b8feca895a8fd3af52d70fb
---

# Ace Adsgetmemodatatype

AdsGetMemoDataType

AdsGetMemoDataType

Advantage Client Engine

| AdsGetMemoDataType  Advantage Client Engine |  |  |  |  |

Returns the specific type of data stored in a memo field.

Syntax

| UNSIGNED32 | AdsGetMemoDataType (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pusType); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of the field to check memo type. |
| pusType (I) | Buffer in which to return the type of memo. This will be one of the following: ADS\_MEMO, ADS\_BINARY, or ADS\_IMAGE. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

AdsGetMemoDataType is provided for compatibility with other Advantage client development environments, which store binary data in DBF memo fields. If a DBF table has a memo field that is used for storing binary data, then this function can be used to determine the exact type of data stored in the memo field on a record-by-record basis. A type of ADS\_IMAGE indicates that an image is stored in the memo field. ADS\_BINARY indicates that some kind of generic binary data is in the field. If the field is a standard memo, the function will return ADS\_MEMO for pusType. ADT tables cannot store binary and image data in standard character memo fields.

Example

[Click Here](ace_examples.md#adsgetmemodatatypeexample)

See Also

[AdsGetFieldType](ace_adsgetfieldtype.md)

[AdsGetString](ace_adsgetstring.md)

[AdsGetBinary](ace_adsgetbinary.md)

[AdsGetMemoLength](ace_adsgetmemolength.md)

[AdsGetBinaryLength](ace_adsgetbinarylength.md)

[AdsSetBinary](ace_adssetbinary.md)
