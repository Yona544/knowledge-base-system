---
title: Ace Adsisempty
slug: ace_adsisempty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisempty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c064a389a4f79c905fcd2c9eadccb53acf2d2622
---

# Ace Adsisempty

AdsIsEmpty

AdsIsEmpty

Advantage Client Engine

| AdsIsEmpty  Advantage Client Engine |  |  |  |  |

Determines if a given field is empty (null).

Syntax

| UNSIGNED32 | AdsIsEmpty (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pbEmpty); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to query. |
| pbEmpty (O) | Will be True on return if the specified field is empty/null. |

Remarks

Use AdsIsEmpty to determine if the indicated field is NULL for ADTs or empty for DBFs. The NULL/empty value can vary between data types. Therefore, AdsIsEmpty can be used to be certain whether the current field value is NULL/empty.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsisemptyexample)

See Also

[AdsSetEmpty](ace_adssetempty.md)

[AdsSetField](ace_adssetfield.md)

[AdsIsNull](ace_adsisnull.md)
