---
title: Ace Adsgetbinarylength
slug: ace_adsgetbinarylength
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetbinarylength.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: bac6c5b4293daeb3eb035641b05172bbb98823cd
---

# Ace Adsgetbinarylength

AdsGetBinaryLength

AdsGetBinaryLength

Advantage Client Engine

| AdsGetBinaryLength  Advantage Client Engine |  |  |  |  |

Retrieves the length of the specified binary object in the given fields of the current record.

Syntax

| UNSIGNED32 | AdsGetBinaryLength (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED32 \*pulLength); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field containing the binary object. |
| pulLength (O) | Return length of binary object. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF. |

Remarks

AdsGetBinaryLength can be used to determine the amount of memory or disk resources needed to manipulate a binary object.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetbinarylengthexample)

See Also

[AdsGetBinary](ace_adsgetbinary.md)

[AdsFileToBinary](ace_adsfiletobinary.md)

[AdsBinaryToFile](ace_adsbinarytofile.md)
