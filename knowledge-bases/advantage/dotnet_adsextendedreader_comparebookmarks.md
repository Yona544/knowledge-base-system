AdsExtendedReader.CompareBookmarks




Advantage Database Server 12  

AdsExtendedReader.CompareBookmarks

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.CompareBookmarks  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.CompareBookmarks Advantage .NET Data Provider dotnet\_Adsextendedreader\_comparebookmarks Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.CompareBookmarks / Dear Support Staff, |  |
| AdsExtendedReader.CompareBookmarks  Advantage .NET Data Provider |  |  |  |  |

Compares two bookmarks.

public int CompareBookMarks( AdsBookMark bmk1, AdsBookMark bmk2 );

Remarks

Compares two bookmarks. AdsBookmark objects are returned from [GetBookmark](dotnet_adsextendedreader_getbookmark.htm). If the bookmarks were retrieved from an index handle the key values associated with the bookmarks will be compared. Otherwise, the comparison will be based on the record number. If the key values are compared and determined to be equivalent the record number will then be used for the comparison.

See Also

[GetBookmark](dotnet_adsextendedreader_getbookmark.htm)

[GotoBookmark](dotnet_adsextendedreader_gotobookmark.htm)