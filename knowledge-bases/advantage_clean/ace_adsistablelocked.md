---
title: Ace Adsistablelocked
slug: ace_adsistablelocked
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsistablelocked.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: e4649de135cbc405864dc472400e3e79ae11c3cf
---

# Ace Adsistablelocked

AdsIsTableLocked

AdsIsTableLocked

Advantage Client Engine

| AdsIsTableLocked  Advantage Client Engine |  |  |  |  |

Tests if the given table is locked by the current user

Syntax

| UNSIGNED32 | AdsIsTableLocked (ADSHANDLE hTable,  UNSIGNED16 \*pbLocked); |

Parameters

| hTable (I) | Handle of table. |
| pbLocked (O) | Return True if locked, False if not locked. |

Remarks

AdsIsTableLocked will return True if the table is locked by the current user. If the table is locked by another user or by this user who is using a different table handle, AdsIsTableLocked will return False. If the table is opened exclusively by the current user, this function will return False.

Note AdsIsTableLocked only tests for a lock on the given table handle (hTable). It does not test for table locks acquired on other table handles even though they refer to the same physical file.

Example

[Click Here](ace_examples.md#adsistablelockedexample)

See Also

[AdsLockTable](ace_adslocktable.md)

[AdsUnlockTable](ace_adsunlocktable.md)

[AdsLockRecord](ace_adslockrecord.md)
