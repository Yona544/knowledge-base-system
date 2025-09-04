---
title: Dotnet Adsextendedreader Lockrecord
slug: dotnet_adsextendedreader_lockrecord
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_lockrecord.htm
source: Advantage CHM
tags:
  - dotnet
checksum: de4d70c944d0316c9c76b9a504ae65b6be9e0cfc
---

# Dotnet Adsextendedreader Lockrecord

AdsExtendedReader.LockRecord

AdsExtendedReader.LockRecord

Advantage .NET Data Provider

| AdsExtendedReader.LockRecord  Advantage .NET Data Provider |  |  |  |  |

Attempts to lock the current or given record.

public void LockRecord();

 

public void LockRecord(int iRecordNumber);

Remarks

A record lock allows a user to update a shared file. If a record lock is successful, the record is reread. If the given iRecordNumber is zero, the current record is locked. If the record number sent to this function is the number of records in the table + 1, no other users will be able to append records to the table.

Note This function does not perform multiple attempts to lock the record if the lock fails.

See Also

[LockTable](dotnet_adsextendedreader_locktable.md)

[UnlockRecord](dotnet_adsextendedreader_unlockrecord.md)

[IsRecordLocked](dotnet_adsextendedreader_isrecordlocked.md)
