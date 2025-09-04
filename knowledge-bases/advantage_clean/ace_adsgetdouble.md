---
title: Ace Adsgetdouble
slug: ace_adsgetdouble
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdouble.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c806c50185a0d0cfb03acb9ef4de7351ba56330e
---

# Ace Adsgetdouble

AdsGetDouble

AdsGetDouble

Advantage Client Engine

| AdsGetDouble  Advantage Client Engine |  |  |  |  |

Retrieves an 8-byte double value from the given field.

Syntax

| UNSIGNED32 | AdsGetDouble (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  double64 \*pdValue); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pdValue (O) | Return the value. |

Remarks

AdsGetDouble returns the IEEE 64-bit double representation of the value in a numeric, long integer, integer, short integer, double, CurDouble, Money, RowVersion, or autoincrement field. This function provides the largest range available in the Advantage Client Engine for retrieving numeric values. However, since the IEEE 64-bit double value has roughly 15 digits of precision, loss of precision is possible when retrieving values from long integer, Money or numeric field types.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetdoubleexample)

See Also

[AdsSetDouble](ace_adssetdouble.md)

[AdsGetField](ace_adsgetfield.md)

[AdsGetLong](ace_adsgetlong.md)

[AdsGetLongLong](ace_adsgetlonglong.md)
