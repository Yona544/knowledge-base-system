---
title: Ace Adsreindexfts
slug: ace_adsreindexfts
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsreindexfts.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3d45e15ea1fd3c444f8a5d805b5b3b4fa90b9df2
---

# Ace Adsreindexfts

AdsReindexFTS

AdsReindexFTS

Advantage Client Engine

| AdsReindexFTS  Advantage Client Engine |  |  |  |  |

Rebuilds index files that contain only full text search indexes.

Syntax

| UNSIGNED32 | AdsReindexFTS ( ADSHANDLE hTable,  UNSIGNED32 ulPageSize ); |

Parameters

| hTable (I) | Handle of table. |
| ulPageSize (I) | The page size to use when reindexing tables of type ADS\_ADT. It is ignored for tables of type ADS\_CDX and ADS\_VFP. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, then a default page size of 1024 bytes will be used. Refer to [Index Page Size](master_index_page_size.md) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table. If a user connection is used to reindex a table in a data dictionary, ADS\_DEFAULT should be passed as the index page size. |

Remarks

This API rebuilds index files that contain only full text search (FTS) indexes. If an index file contains any non-FTS indexes, then it will not be rebuilt by a call to this API. Use [AdsReindex61](ace_adsreindex61.md) to reindex all indexes on a table (including FTS indexes).

Note Calling AdsReindexFTS inside a transaction is illegal.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.md)

[AdsReindex61](ace_adsreindex61.md)
