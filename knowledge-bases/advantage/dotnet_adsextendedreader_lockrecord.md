AdsExtendedReader.LockRecord




Advantage Database Server 12  

AdsExtendedReader.LockRecord

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.LockRecord  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.LockRecord Advantage .NET Data Provider dotnet\_Adsextendedreader\_lockrecord Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.LockRecord / Dear Support Staff, |  |
| AdsExtendedReader.LockRecord  Advantage .NET Data Provider |  |  |  |  |

Attempts to lock the current or given record.

public void LockRecord();

 

public void LockRecord(int iRecordNumber);

Remarks

A record lock allows a user to update a shared file. If a record lock is successful, the record is reread. If the given iRecordNumber is zero, the current record is locked. If the record number sent to this function is the number of records in the table + 1, no other users will be able to append records to the table.

Note This function does not perform multiple attempts to lock the record if the lock fails.

See Also

[LockTable](dotnet_adsextendedreader_locktable.htm)

[UnlockRecord](dotnet_adsextendedreader_unlockrecord.htm)

[IsRecordLocked](dotnet_adsextendedreader_isrecordlocked.htm)