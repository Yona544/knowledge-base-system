---
title: Dotnet Adsextendedreader Deleteindex
slug: dotnet_adsextendedreader_deleteindex
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_deleteindex.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 44f7522e8f1c62290cd2d89c2ee1dcb4f6e3ca3f
---

# Dotnet Adsextendedreader Deleteindex

AdsExtendedReader.DeleteIndex

AdsExtendedReader.DeleteIndex

Advantage .NET Data Provider

| AdsExtendedReader.DeleteIndex  Advantage .NET Data Provider |  |  |  |  |

Deletes the actively selected index.

public void DeleteIndex();

Remarks

The actively selected index will be deleted when this is called. The table must be opened exclusively for this to succeed (use "shared=false;" in the connection string). If the index order is a tag in a CDX or ADI file, the tag will be marked for deletion and will no longer be used. If it is the last non-deleted tag in the file, the physical file will be deleted. If the index order is an IDX or NTX, the file will be deleted. Remove deleted tags out of compound index files by reindexing (see [AdsExtendedReader.Reindex](dotnet_adsextendedreader_reindex.md)).

See Also

[CreateIndex](dotnet_adsextendedreader_createindex.md)

[ActiveIndex](dotnet_adsextendedreader_activeindex.md)
