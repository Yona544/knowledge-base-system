---
title: Ace Adsgetmemolength
slug: ace_adsgetmemolength
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetmemolength.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 892989b8f02007d073dac5ac15e0e75275c2f22f
---

# Ace Adsgetmemolength

AdsGetMemoLength

AdsGetMemoLength

Advantage Client Engine

| AdsGetMemoLength  Advantage Client Engine |  |  |  |  |

Retrieves the length of the specified memo field of the current record.

Syntax

| UNSIGNED32 | AdsGetMemoLength (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 \*pulLength); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of memo field. |
| pulLength (O) | Return length of memo. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

AdsGetMemoLength returns the length of the specified memo field in characters.  For Unicode memo fields of type ADS\_NMEMO this is the number of 16-bit code units.  For memo fields of type ADS\_MEMO, the length in characters is the same as the length in bytes. AdsGetMemoLength will not support binary object fields. Use [AdsGetBinaryLength](ace_adsgetbinarylength.md) for binary fields.

Example

[Click Here](ace_examples.md#adsgetmemolengthexample)

See Also

[AdsGetFieldType](ace_adsgetfieldtype.md)

[AdsGetFieldLength](ace_adsgetfieldlength.md)

[AdsGetString](ace_adsgetstring.md)

[AdsGetField](ace_adsgetfield.md)

[AdsGetMemoDataType](ace_adsgetmemodatatype.md)
