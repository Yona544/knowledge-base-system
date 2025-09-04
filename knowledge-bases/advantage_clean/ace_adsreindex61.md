---
title: Ace Adsreindex61
slug: ace_adsreindex61
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsreindex61.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 52e012cb920f5567c6a30c04b2fafea2da6a1030
---

# Ace Adsreindex61

AdsReindex61

AdsReindex61

Advantage Client Engine

| AdsReindex61  Advantage Client Engine |  |  |  |  |

Rebuilds all open indexes associated with the given table

Syntax

| UNSIGNED32 | AdsReindex61 (ADSHANDLE hTable,  UNSIGNED32 ulPageSize); |

Parameters

| hTable (I) | Handle of table. |
| ulPageSize (I) | The page size to use when reindexing tables of type ADS\_ADT. It is ignored for tables of type ADS\_NTX, ADS\_VFP and ADS\_CDX. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, the existing page size is used. Refer to [Index Page Size](master_index_page_size.md) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table. If a user connection is used to reindex a table in a data dictionary, ADS\_DEFAULT should be passed as the index page size. |

Remarks

AdsReindex61 requires exclusive use of the open indexes. A reindex will rebuild all keys in all open index orders for the table. It is unlikely that reindexing will be necessary if only Advantage applications are using data. If other applications not using Advantage are using data, however, there is a possibility for index corruption to occur. Reindexing occurs automatically when calls are made to [AdsPackTable](ace_adspacktable.md) and [AdsZapTable](ace_adszaptable.md). Calling AdsReindex61 on a CDX or ADI index that contains a custom index order will results in all keys being removed from the custom index order.

Note Calling AdsReindex61 inside a transaction is illegal.

 

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

Example

[Click Here](ace_examples.md#adsreindexexample)

See Also

[sp\_Reindex](master_sp_reindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsReindex](ace_adsreindex.md)

[AdsRegisterProgressCallback](ace_adsregisterprogresscallback.md)
