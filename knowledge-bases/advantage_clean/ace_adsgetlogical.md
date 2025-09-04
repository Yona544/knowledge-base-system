---
title: Ace Adsgetlogical
slug: ace_adsgetlogical
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetlogical.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 79110acff600c20451c8b1fab29e1faba43a0e3d
---

# Ace Adsgetlogical

AdsGetLogical

AdsGetLogical

Advantage Client Engine

| AdsGetLogical  Advantage Client Engine |  |  |  |  |

Retrieves logical value from the given field.

Syntax

| UNSIGNED32 | AdsGetLogical (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pbValue); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pbValue (O) | Return the value. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

The value returned in pbValue will be either True (1) or False (0). AdsGetLogical also returns False if the logical field contains a NULL value. To determine if a False return type is NULL or assigned to False, call [AdsIsEmpty](ace_adsisempty.md) or [AdsGetString](ace_adsgetstring.md) on the logical field.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetlogicalexample)

See Also

[AdsGetField](ace_adsgetfield.md)

[AdsSetLogical](ace_adssetlogical.md)
