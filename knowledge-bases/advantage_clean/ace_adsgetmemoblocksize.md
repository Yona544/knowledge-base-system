---
title: Ace Adsgetmemoblocksize
slug: ace_adsgetmemoblocksize
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetmemoblocksize.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d81c49043ee134c8e2ca6a418d42be1a45774c95
---

# Ace Adsgetmemoblocksize

AdsGetMemoBlockSize

AdsGetMemoBlockSize

Advantage Client Engine

| AdsGetMemoBlockSize  Advantage Client Engine |  |  |  |  |

Returns the block size of a memo file associated with a table or cursor.

Syntax

| UNSIGNED32 | AdsGetMemoBlockSize (ADSHANDLE hTable,  UNSIGNED16 \*pusBlockSize); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusBlockSize (I) | Buffer in which to return the memo block size. |

Special Return Codes

| AE\_NO\_MEMO\_FILE | The table or cursor handle must have an associated memo file. |

Remarks

AdsGetMemoBlockSize returns the memo block size of the memo file associated with the table or SQL cursor handle. The memo block size can be configured when creating a table via the [AdsCreateTable](ace_adscreatetable.md) ACE API. Note that DBF/NTX (ADS\_NTX) type tables and cursors always have a memo block size of 512.

See Also

[AdsGetMemoLength](ace_adsgetmemolength.md)

[AdsGetMemoDataType](ace_adsgetmemodatatype.md)

[AdsCreateTable](ace_adscreatetable.md)
