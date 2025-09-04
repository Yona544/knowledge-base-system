---
title: Dotnet Adsextendedreader Comparebookmarks
slug: dotnet_adsextendedreader_comparebookmarks
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_comparebookmarks.htm
source: Advantage CHM
tags:
  - dotnet
checksum: aeebcedaa2c9c780dd4963b0e2a841b02b1701b5
---

# Dotnet Adsextendedreader Comparebookmarks

AdsExtendedReader.CompareBookmarks

AdsExtendedReader.CompareBookmarks

Advantage .NET Data Provider

| AdsExtendedReader.CompareBookmarks  Advantage .NET Data Provider |  |  |  |  |

Compares two bookmarks.

public int CompareBookMarks( AdsBookMark bmk1, AdsBookMark bmk2 );

Remarks

Compares two bookmarks. AdsBookmark objects are returned from [GetBookmark](dotnet_adsextendedreader_getbookmark.md). If the bookmarks were retrieved from an index handle the key values associated with the bookmarks will be compared. Otherwise, the comparison will be based on the record number. If the key values are compared and determined to be equivalent the record number will then be used for the comparison.

See Also

[GetBookmark](dotnet_adsextendedreader_getbookmark.md)

[GotoBookmark](dotnet_adsextendedreader_gotobookmark.md)
