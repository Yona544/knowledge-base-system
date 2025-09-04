---
title: Ace Adsreindex
slug: ace_adsreindex
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsreindex.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 507021990bfea132e9f3f795237c2c47a3bbc693
---

# Ace Adsreindex

AdsReindex

AdsReindex

Advantage Client Engine

| AdsReindex  Advantage Client Engine |  |  |  |  |

Rebuilds all open indexes associated with the given table.

Syntax

| UNSIGNED32 | AdsReindex (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table. |

Remarks

AdsReindex requires exclusive use of the open indexes. A reindex will rebuild all keys in all open index orders for the table. It is unlikely that reindexing will be necessary if only Advantage applications are using data. If other applications not using Advantage are using data, however, there is a possibility for index corruption to occur. Reindexing occurs automatically when calls are made to [AdsPackTable](ace_adspacktable.md) and [AdsZapTable](ace_adszaptable.md). Calling AdsReindex on a CDX or ADI index that contains a custom index order will results in all keys being removed from the custom index order.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note Calling AdsReindex inside a transaction is illegal.

 

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

Example

[Click Here](ace_examples.md#adsreindexexample)

See Also

[sp\_Reindex](master_sp_reindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsRegisterProgressCallback](ace_adsregisterprogresscallback.md)

[AdsReindex61](ace_adsreindex61.md)
