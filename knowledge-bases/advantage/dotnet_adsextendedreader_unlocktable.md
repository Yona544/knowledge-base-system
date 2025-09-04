AdsExtendedReader.UnlockTable




Advantage Database Server 12  

AdsExtendedReader.UnlockTable

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.UnlockTable  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.UnlockTable Advantage .NET Data Provider dotnet\_Adsextendedreader\_unlocktable Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.UnlockTable / Dear Support Staff, |  |
| AdsExtendedReader.UnlockTable  Advantage .NET Data Provider |  |  |  |  |

Releases all locks on the given table

public void UnlockTable();

Remarks

AdsUnlockTable releases either all record locks on the table, or a table lock if one exists. If record locks are held and the table is in a transaction, the record locks will be released at the end of the transaction.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error.

See Also

[LockRecord](dotnet_adsextendedreader_lockrecord.htm)

[LockTable](dotnet_adsextendedreader_locktable.htm)

[IsTableLocked](dotnet_adsextendedreader_istablelocked.htm)

[UnlockRecord](dotnet_adsextendedreader_unlockrecord.htm)