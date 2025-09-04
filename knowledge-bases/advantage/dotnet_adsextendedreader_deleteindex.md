AdsExtendedReader.DeleteIndex




Advantage Database Server 12  

AdsExtendedReader.DeleteIndex

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.DeleteIndex  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.DeleteIndex Advantage .NET Data Provider dotnet\_Adsextendedreader\_deleteindex Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.DeleteIndex / Dear Support Staff, |  |
| AdsExtendedReader.DeleteIndex  Advantage .NET Data Provider |  |  |  |  |

Deletes the actively selected index.

public void DeleteIndex();

Remarks

The actively selected index will be deleted when this is called. The table must be opened exclusively for this to succeed (use "shared=false;" in the connection string). If the index order is a tag in a CDX or ADI file, the tag will be marked for deletion and will no longer be used. If it is the last non-deleted tag in the file, the physical file will be deleted. If the index order is an IDX or NTX, the file will be deleted. Remove deleted tags out of compound index files by reindexing (see [AdsExtendedReader.Reindex](dotnet_adsextendedreader_reindex.htm)).

See Also

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[ActiveIndex](dotnet_adsextendedreader_activeindex.htm)