---
title: Ace Adsisnull
slug: ace_adsisnull
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisnull.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e8b103d2a5ab7ed17cc0f30445fa9ed6ab7d8a59
---

# Ace Adsisnull

AdsIsNull

AdsIsNull

Advantage Client Engine

| AdsIsNull  Advantage Client Engine |  |  |  |  |

Determines if a given field is NULL.

Syntax

| UNSIGNED32 | AdsIsNull (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED16 \*pbNull); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to query. |
| pbNull (O) | Will be True on return if the specified field is NULL. |

Remarks

For table types ADS\_ADT, ADS\_NTX, and ADS\_CDX, this API behaves identically to [AdsIsEmpty](ace_adsisempty.md). Use AdsIsNull to determine if the indicated field is NULL for ADT and VFP tables or empty for non-VFP DBFs.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

See Also

[AdsSetNull](ace_adssetnull.md)

[AdsIsEmpty](ace_adsisempty.md)
