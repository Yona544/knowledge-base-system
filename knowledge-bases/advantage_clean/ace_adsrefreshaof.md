---
title: Ace Adsrefreshaof
slug: ace_adsrefreshaof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsrefreshaof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c53d65b961d94d8826f92e28cfd9da28c5b5f2c8
---

# Ace Adsrefreshaof

AdsRefreshAOF

AdsRefreshAOF

Advantage Client Engine

| AdsRefreshAOF  Advantage Client Engine |  |  |  |  |

Updates the filter

Syntax

| UNSIGNED32 | AdsRefreshAOF ( ADSHANDLE hTable ); |

Parameters

| hTable (I) | Handle of a table or cursor that has an AOF to be refreshed. |

Remarks

AdsRefreshAOF rebuilds the filter using the original values passed to [AdsSetAOF](ace_adssetaof.md). The [Advantage Database Server](master_advantage_database_server.md) maintains the accuracy of all AOFs associated with a given table when updates are performed. With [Advantage Local Server](master_advantage_local_server.md), however, it is possible for another client to make updates to the table. In that case, it might be useful to call AdsRefreshAOF to force the filter to be rebuilt. It may also make sense to call this function if an index that could affect the optimization level of the AOF has been opened or created since the original AOF was created.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

[Click Here](ace_aof_and_encryption_examples.md#adsrefreshaof_example)

See Also

[AdsSetAOF](ace_adssetaof.md)

[AdsClearAOF](ace_adsclearaof.md)

[AdsGetAOF](ace_adsgetaof.md)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.md)

[AdsEvalAOF](ace_adsevalaof.md)
