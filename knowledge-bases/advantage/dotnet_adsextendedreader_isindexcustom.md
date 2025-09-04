AdsExtendedReader.IsIndexCustom




Advantage Database Server 12  

AdsExtendedReader.IsIndexCustom

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.IsIndexCustom  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.IsIndexCustom Advantage .NET Data Provider dotnet\_Adsextendedreader\_isindexcustom Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.IsIndexCustom / Dear Support Staff, |  |
| AdsExtendedReader.IsIndexCustom  Advantage .NET Data Provider |  |  |  |  |

Tests the active index to determine if it is a custom index.

public bool IsIndexCustom{ get; }

Remarks

This property returns true if the current index order is a custom index. Custom indexes are indexes that are not maintained by Advantage. An application must add and delete the keys. The Advantage .NET Data Provider does not provide the means to create or maintain custom indexes.

See Also

[AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.htm)