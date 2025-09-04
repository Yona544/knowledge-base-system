---
title: Ade Adssetaof
slug: ade_adssetaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1aa626219e692f927b708b4e9f38b77b55cdf690
---

# Ade Adssetaof

AdsSetAOF

TAdsTable.AdsSetAOF

Advantage TDataSet Descendant

| TAdsTable.AdsSetAOF  Advantage TDataSet Descendant |  |  |  |  |

Create an Advantage Optimized Filter (AOF) for the given table.

Syntax

procedure AdsSetAOF ( strFilter : String );

Parameter

| strFilter | filter expression. |

Description

AdsSetAOF creates an Advantage Optimized Filter on the given table using all currently open indexes. Advantage Optimized Filters (AOF) provide state of the art filter optimization for Advantage Client Engine applications. AOFs speed filter processing by using index keys instead of table records. If a specified field has an index built on it, then an AOF uses the index file rather than the table to process the query. Performance is increased by reducing the amount of data that must be retrieved from the disk. Changes made by other users to records in the table that affect inclusion in the AOF are not automatically reflected in the AOF, however.

Use of Advantage Optimized Filters rather than traditional record filters is the default behavior for the Filter property inherited from native Delphi in TAdsTable.

Note AdsSetAOF is only optimized for use with tables that were opened with ttAdsCDX, ttAdsVFP and ttAdsADT as the table type. The AOF will work with a table that was opened with ttAdsNTX, but will act more like a normal filter.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

AdsTable1.AdsClearAOF;

See Also

[AdsClearAOF](ade_adsclearaof.md)

[AdsRefreshAOF](ade_adsrefreshaof.md)

[AdsGetAOF](ade_adsgetaof.md)

[AdsEvalAOF](ade_adsevalaof.md)

[AdsSetFilter](ade_adssetfilter.md)

[AdsCustomizeAOF](ade_adscustomizeaof.md)

[AdsIsRecordInAOF](ade_adsisrecordinaof.md)

[AdsAOFType](ade_adsaoftype.md)
