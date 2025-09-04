---
title: Dotnet Adsextendedreader Reindex
slug: dotnet_adsextendedreader_reindex
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_reindex.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 65093d12fe5c3aa2ed8208d51aa88d36c76aeefe
---

# Dotnet Adsextendedreader Reindex

AdsExtendedReader.Reindex

AdsExtendedReader.Reindex

Advantage .NET Data Provider

| AdsExtendedReader.Reindex  Advantage .NET Data Provider |  |  |  |  |

Rebuilds all open indexes.

public void Reindex();

public void Reindex( int iPageSize );

Remarks

Reindex requires exclusive use of the open indexes. A reindex will rebuild all keys in all open index orders for the table. It is unlikely that reindexing will be necessary if only Advantage applications are using data. If other applications not using Advantage are using data, however, there is a possibility for index corruption to occur. Reindexing occurs automatically when calls are made to [PackTable](dotnet_adsextendedreader_packtable.md) and [ZapTable](dotnet_adsextendedreader_zaptable.md). Calling Reindex on a CDX or ADI index that contains a custom index order will results in all keys being removed from the custom index order.

IPageSize is the page size to use when reindexing tables of type ADT. It is ignored for tables of [TableType](dotnet_adsextendedreader_tabletype.md) NTX, VFP, and CDX. Valid values are any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If no size is given, then the default page size of 512 bytes will be used. Refer to [Index Page Size](master_index_page_size.md) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table.

Note Calling Reindex inside a transaction is illegal.

 

Note Reindex operates only on tables. The use of a cursors with Reindex is illegal and will result in an exception.

See Also

[OpenIndex](dotnet_adsextendedreader_openindex.md)

[CreateIndex](dotnet_adsextendedreader_createindex.md)

[Progress](dotnet_adsextendedreader_progress.md)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.md)

[Cancel](dotnet_adsextendedreader_cancel.md)
