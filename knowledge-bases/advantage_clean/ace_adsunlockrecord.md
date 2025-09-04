---
title: Ace Adsunlockrecord
slug: ace_adsunlockrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsunlockrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 405efae768fdca9bb665060607c41e9a3196e6a3
---

# Ace Adsunlockrecord

AdsUnlockRecord

AdsUnlockRecord

Advantage Client Engine

| AdsUnlockRecord  Advantage Client Engine |  |  |  |  |

Unlocks the given record

Syntax

| UNSIGNED32 | AdsUnlockRecord (ADSHANDLE hTable,  UNSIGNED32 ulRec); |

Parameters

| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number to unlock. If zero, then unlock the current record. |

Special Return Codes

| AE\_RECORD\_NOT\_LOCKED | The indicated record was not locked. |
| AE\_INVALID\_RECORD\_NUMBER | The record number given was not valid. |

Remarks

AdsUnlockRecord releases the servers lock on the record and flushes any changes in the record to disk.

Note Records cannot be unlocked on the server during transactions. Therefore, calls to AdsUnlockRecord during a transaction will cause the Advantage Client Engine to mark the record lock as "unlocked during transaction", and the Advantage Client Engine will release the lock at the end (commit or rollback) of the transaction.

Example

[Click Here](ace_examples.md#adsunlockrecordexample)

See Also

[AdsLockRecord](ace_adslockrecord.md)

[AdsIsRecordLocked](ace_adsisrecordlocked.md)

[AdsLockTable](ace_adslocktable.md)

[AdsGetAllLocks](ace_adsgetalllocks.md)

[AdsUnlockTable](ace_adsunlocktable.md)
