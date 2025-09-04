---
title: Ace Adslockrecord
slug: ace_adslockrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adslockrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 92594c13ea9d81b19eb286ce30aa1d9f80f7d807
---

# Ace Adslockrecord

AdsLockRecord

AdsLockRecord

Advantage Client Engine

| AdsLockRecord  Advantage Client Engine |  |  |  |  |

Attempts to lock the given record

Syntax

| UNSIGNED32 | AdsLockRecord (ADSHANDLE hTable,  UNSIGNED32 ulRec); |

Parameters

| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number to lock. |

Special Return Codes

| AE\_LOCK\_FAILED | The attempted lock failed. The lock may be held by another user. |
| AE\_TABLE\_NOT\_SHARED | A lock was attempted on a table opened exclusively. |

Remarks

A record lock allows a user to update a shared file. If the table is already file locked or opened exclusively, this function returns AE\_SUCCESS. If a record lock is successful, the record is reread. If zero is sent from ulRec, the current record is locked. If the record number sent to this function is the number of records in the table + 1, no other users will be able to append records to the table.

Note AdsLockRecord does not perform multiple attempts to lock the record if the lock fails.

Example

[Click Here](ace_examples.md#adslockrecordexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsLockTable](ace_adslocktable.md)

[AdsUnlockRecord](ace_adsunlockrecord.md)

[AdsIsRecordLocked](ace_adsisrecordlocked.md)

[AdsGetAllLocks](ace_adsgetalllocks.md)
