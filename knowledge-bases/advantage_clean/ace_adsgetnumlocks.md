---
title: Ace Adsgetnumlocks
slug: ace_adsgetnumlocks
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetnumlocks.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 96bd2269645b0e638956e328e8f7949239aabd0b
---

# Ace Adsgetnumlocks

AdsGetNumLocks

AdsGetNumLocks

Advantage Client Engine

| AdsGetNumLocks  Advantage Client Engine |  |  |  |  |

Retrieves the total number of records locked by the current user on the given table

Syntax

| UNSIGNED32 | AdsGetNumLocks (ADSHANDLE hTable,  UNSIGNED16 \*pusNum); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusNum (O) | Return number of locks. |

Remarks

AdsGetNumLocks returns zero in pulNum if the table is file locked. The number of locks returned includes implicit locks. The number does not include locks held by other users or other applications.

Example

[Click Here](ace_examples.md#adsgetnumlocksexample)

See Also

[AdsGetAllLocks](ace_adsgetalllocks.md)

[AdsLockRecord](ace_adslockrecord.md)

[AdsUnlockRecord](ace_adsunlockrecord.md)

[AdsIsRecordLocked](ace_adsisrecordlocked.md)

[AdsLockTable](ace_adslocktable.md)
