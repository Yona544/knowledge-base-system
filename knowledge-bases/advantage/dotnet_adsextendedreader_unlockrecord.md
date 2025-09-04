AdsExtendedReader.UnlockRecord




Advantage Database Server 12  

AdsExtendedReader.UnlockRecord

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.UnlockRecord  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.UnlockRecord Advantage .NET Data Provider dotnet\_Adsextendedreader\_unlockrecord Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.UnlockRecord / Dear Support Staff, |  |
| AdsExtendedReader.UnlockRecord  Advantage .NET Data Provider |  |  |  |  |

Unlocks the current or given record

public void UnlockRecord();

 

public void UnlockRecord(int iRecordNumber);

Remarks

UnlockRecord releases the servers lock on the record and flushes any changes in the record to disk.

Note Records cannot be unlocked on the server during transactions. Therefore, calls to UnlockRecord during a transaction will cause the Advantage Client Engine to mark the record lock as "unlocked during transaction", and the Advantage Client Engine will release the lock at the end (commit or rollback) of the transaction.

See Also

[LockRecord](dotnet_adsextendedreader_lockrecord.htm)

[IsRecordLocked](dotnet_adsextendedreader_isrecordlocked.htm)

[LockTable](dotnet_adsextendedreader_locktable.htm)

[UnlockTable](dotnet_adsextendedreader_unlocktable.htm)