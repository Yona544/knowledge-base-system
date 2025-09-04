---
title: Ade Adsrefreshaof
slug: ade_adsrefreshaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsrefreshaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 83c90f39bd5e78f2d4ae95ae0806242ef945a1af
---

# Ade Adsrefreshaof

AdsRefreshAOF

TAdsTable/TAdsQuery.AdsRefreshAOF

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsRefreshAOF  Advantage TDataSet Descendant |  |  |  |  |

Rebuilds the filter.

Syntax

procedure AdsRefreshAOF;

Description

AdsRefreshAOF rebuilds the filter using the original values passed to [AdsSetAOF](ade_adssetaof.md). The [Advantage Database Server](master_advantage_database_server.md) maintains the accuracy of all AOFs associated with a given table when updates are performed. With [Advantage Local Server](master_advantage_local_server.md), however, it is possible for another client to make updates to the table. In that case, it might be useful to call AdsRefreshAOF to force the filter to be rebuilt. It may also make sense to call this function if an index that could affect the optimization level of the AOF has been opened or created since the original AOF was created.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

AdsTable1.AdsRefreshAOF;

 

See Also

[AdsSetAOF](ade_adssetaof.md)

[AdsClearAOF](ade_adsclearaof.md)

[AdsGetAOF](ade_adsgetaof.md)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.md)

[AdsEvalAOF](ade_adsevalaof.md)
