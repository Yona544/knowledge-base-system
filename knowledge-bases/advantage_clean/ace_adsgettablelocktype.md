---
title: Ace Adsgettablelocktype
slug: ace_adsgettablelocktype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablelocktype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 845e67548688c6c3aa9de5b5511a1d05379d783e
---

# Ace Adsgettablelocktype

AdsGetTableLockType

AdsGetTableLockType

Advantage Client Engine

| AdsGetTableLockType  Advantage Client Engine |  |  |  |  |

Retrieves the type of locking used with the table

Syntax

| UNSIGNED32 | AdsGetTableLockType (ADSHANDLE hTable,  UNSIGNED16 \*pusLockType); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusLockType (O) | Type of locking used for table (ADS\_PROPRIETARY\_LOCKING, ADS\_COMPATIBLE\_LOCKING). |

Remarks

AdsGetTableLockType will retrieve the setting of the type of locking specified during the table open/create. See [Advantage Locking Modes](master_advantage_locking_modes.md) for more information on Advantage locking options. Note that if the usTableType parameter used in the open/create was ADS\_ADT, ADS\_PROPRIETARY\_LOCKING will always be returned when using the Advantage Database Server, and ADS\_COMPATIBLE\_LOCKING will always be returned when using the Advantage Local Server.

Example

[Click Here](ace_examples.md#adsgettablelocktypeexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)
