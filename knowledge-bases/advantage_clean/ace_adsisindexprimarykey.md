---
title: Ace Adsisindexprimarykey
slug: ace_adsisindexprimarykey
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisindexprimarykey.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: adf80ffcc378afb746059c67b436ced6d941b14d
---

# Ace Adsisindexprimarykey

AdsIsIndexPrimaryKey

AdsIsIndexPrimaryKey

Advantage Client Engine

| AdsIsIndexPrimaryKey  Advantage Client Engine |  |  |  |  |

Determines if the given index order is the primary key.

Syntax

| UNSIGNED32 | AdsIsIndexPrimaryKey (ADSHANDLE hIndex,  UNSIGNED16 \*pbPrimaryKey); |

Parameters

| hIndex (I) | Handle of index order of interest. |
| pbPrimaryKey (O) | Returns True if index order is the primary key. |

Remarks

Returns True if the index handle provided is the table's primary key.

See Also

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)
