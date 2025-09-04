---
title: Ade Adsreindex
slug: ade_adsreindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsreindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0eab2f7c73ed3d5df52bdce47974f191c5af9dad
---

# Ade Adsreindex

AdsReindex

TAdsTable.AdsReindex

Advantage TDataSet Descendant

| TAdsTable.AdsReindex  Advantage TDataSet Descendant |  |  |  |  |

Rebuilds all open indexes associated with the given table.

Syntax

procedure AdsReindex;

Description

AdsReindex requires exclusive use of the open indexes. A reindex will rebuild all keys in all open index orders for the table. It is unlikely that reindexing will be necessary if only Advantage applications are using data. If other applications not using Advantage are using data, however, there is a possibility for index corruption to occur. Reindexing occurs automatically when calls are made to [AdsPackTable](ade_adspacktable.md) and [AdsZapTable](ade_adszaptable.md).

When reindexing ADT tables, the [AdsIndexPageSize](ade_adsindexpagesize.md) property will be respected. See [Index Page Size](master_index_page_size.md) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note Calling AdsReindex inside a transaction is illegal.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsReindex;

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsOpenIndex](ade_adsopenindex.md)

[AdsRegisterProgressCallback](ade_adsregisterprogresscallback.md)

[AdsIndexPageSize](ade_adsindexpagesize.md)
