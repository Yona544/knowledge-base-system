---
title: Dotnet Adsextendedreader Unlockrecord
slug: dotnet_adsextendedreader_unlockrecord
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_unlockrecord.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2635c57dfea6dd16f083f80c1130cb675c00a624
---

# Dotnet Adsextendedreader Unlockrecord

AdsExtendedReader.UnlockRecord

AdsExtendedReader.UnlockRecord

Advantage .NET Data Provider

| AdsExtendedReader.UnlockRecord  Advantage .NET Data Provider |  |  |  |  |

Unlocks the current or given record

public void UnlockRecord();

 

public void UnlockRecord(int iRecordNumber);

Remarks

UnlockRecord releases the servers lock on the record and flushes any changes in the record to disk.

Note Records cannot be unlocked on the server during transactions. Therefore, calls to UnlockRecord during a transaction will cause the Advantage Client Engine to mark the record lock as "unlocked during transaction", and the Advantage Client Engine will release the lock at the end (commit or rollback) of the transaction.

See Also

[LockRecord](dotnet_adsextendedreader_lockrecord.md)

[IsRecordLocked](dotnet_adsextendedreader_isrecordlocked.md)

[LockTable](dotnet_adsextendedreader_locktable.md)

[UnlockTable](dotnet_adsextendedreader_unlocktable.md)
