AdsExtendedReader.IsTableLocked




Advantage Database Server 12  

AdsExtendedReader.IsTableLocked

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.IsTableLocked  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.IsTableLocked Advantage .NET Data Provider dotnet\_Adsextendedreader\_istablelocked Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.IsTableLocked / Dear Support Staff, |  |
| AdsExtendedReader.IsTableLocked  Advantage .NET Data Provider |  |  |  |  |

Tests if the table is locked by the current user.

public bool IsTableLocked();

Remarks

IsTableLocked can be used to test if the table is locked by the current user. If the table is locked by another user or by the current user with a different reader, IsTableLocked will return false.

See Also

[LockTable](dotnet_adsextendedreader_locktable.htm)

[UnlockTable](dotnet_adsextendedreader_unlocktable.htm)