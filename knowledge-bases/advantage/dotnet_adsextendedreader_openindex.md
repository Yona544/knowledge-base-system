AdsExtendedReader.OpenIndex




Advantage Database Server 12  

AdsExtendedReader.OpenIndex

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.OpenIndex  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.OpenIndex Advantage .NET Data Provider dotnet\_Adsextendedreader\_openindex Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.OpenIndex / Dear Support Staff, |  |
| AdsExtendedReader.OpenIndex  Advantage .NET Data Provider |  |  |  |  |

Opens an index file and associates all index orders in the file with the open table.

public void OpenIndex( string strFileName );

Remarks

OpenIndex retrieves all handles of index orders in the given index file. If the index file is NOT a compound index (CDX or ADI), then it will have only one index order. If the index file is a compound CDX or ADI index, however, more than one index order handle may be returned.

Non-compact IDX files are not supported.

Opening an index does not change the current record.

See Also

[GetIndexNames](dotnet_adsextendedreader_getindexnames.htm)

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[ActiveIndex](dotnet_adsextendedreader_activeindex.htm)