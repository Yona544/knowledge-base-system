AdsExtendedReader.LockTable




Advantage Database Server 12  

AdsExtendedReader.LockTable

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.LockTable  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.LockTable Advantage .NET Data Provider dotnet\_Adsextendedreader\_locktable Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.LockTable / Dear Support Staff, |  |
| AdsExtendedReader.LockTable  Advantage .NET Data Provider |  |  |  |  |

Attempts to lock the table.

public void LockTable();

Remarks

A successful call to LockTable prevents other applications from being able to update the table. It is recommended that you lock tables prior to creating indexes. Any record locks that have been obtained prior to calling LockTable will be released. If the Advantage Client Engine fails to lock the table (e.g., if another user has record locks), then the Advantage Client Engine does not attempt to relock the records that it released.

Note This API only works with tables. The use of cursors with this API is illegal and will result in an exception.

See Also

[LockTable](dotnet_adsextendedreader_locktable.htm)

[UnlockTable](dotnet_adsextendedreader_unlocktable.htm)

[IsTableLocked](dotnet_adsextendedreader_istablelocked.htm)