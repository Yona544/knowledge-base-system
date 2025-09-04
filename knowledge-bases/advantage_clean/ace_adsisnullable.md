---
title: Ace Adsisnullable
slug: ace_adsisnullable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisnullable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d5911108af37d783b1e877a7473e7684b82358f7
---

# Ace Adsisnullable

AdsIsNullable

AdsIsNullable

Advantage Client Engine

| AdsIsNullable  Advantage Client Engine |  |  |  |  |

Determines if a given field can be set to NULL.

Syntax

| UNSIGNED32 | AdsIsNullable (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pbNullable); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to examine. |
| pbNull (O) | Will be True on return if the specified field can store NULL. |

Remarks

This API is primarily intended for the VFP table type to be able to determine if a specific column was created with a NULL or NOT NULL option.  See [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.md). It can, however, be used with other table types and will return the appropriate value.  For example, it will return FALSE for an AUTOINC field and TRUE for an INTEGER field an an ADT table.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

See Also

[AdsSetNull](ace_adssetnull.md)

[AdsIsNull](ace_adsisnull.md)
