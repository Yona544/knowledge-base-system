AdsExtendedReader.GetIndexNames




Advantage Database Server 12  

AdsExtendedReader.GetIndexNames

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.GetIndexNames  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.GetIndexNames Advantage .NET Data Provider dotnet\_Adsextendedreader\_getindexnames Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.GetIndexNames / Dear Support Staff, |  |
| AdsExtendedReader.GetIndexNames  Advantage .NET Data Provider |  |  |  |  |

Returns an object array of index names for the given table.

public object[] GetIndexNames(); // (I) Name of file for new index order.

Remarks

The index names are returned in the order they were opened. For CDX and ADI indexes, the index names are returned in the order they were created within the index file.

See Also

[OpenIndex](dotnet_adsextendedreader_openindex.htm)

[ActiveIndex](dotnet_adsextendedreader_activeindex.htm)