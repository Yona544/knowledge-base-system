---
title: Dotnet Adsextendedreader Isrecordlocked
slug: dotnet_adsextendedreader_isrecordlocked
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_isrecordlocked.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 463325dd96061e328f63c61d8f1f08bf841fda80
---

# Dotnet Adsextendedreader Isrecordlocked

AdsExtendedReader.IsRecordLocked

AdsExtendedReader.IsRecordLocked

Advantage .NET Data Provider

| AdsExtendedReader.IsRecordLocked  Advantage .NET Data Provider |  |  |  |  |

Tests if a record is locked by the current user.

public bool IsRecordLocked();

public bool IsRecordLocked(int iRecordNumber);

Remarks

IsRecordLocked can be used to test if a record is either explicitly or implicitly locked by the current user. The method without parameters checks the lock state of the current record. If the table is locked, IsRecordLocked will return false. If the record or table is locked by another user or by the user that is using a different table handle, IsRecordLocked will return false.

Note IsRecordLocked only tests for record locks on the given reader. It does not test for locks acquired on any other reader even if they refer to the same physical table. It is very fast because it uses the client-side lock list associated with the table rather than making a server request.

See Also

[LockRecord](dotnet_adsextendedreader_lockrecord.md)

[UnlockRecord](dotnet_adsextendedreader_unlockrecord.md)
