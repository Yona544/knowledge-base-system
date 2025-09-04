---
title: Ade Adsgetaof
slug: ade_adsgetaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6b106fa443ac45f958ca6fcc3440a8ab51b0fde8
---

# Ade Adsgetaof

AdsGetAOF

TAdsTable.AdsGetAOF

Advantage TDataSet Descendant

| TAdsTable.AdsGetAOF  Advantage TDataSet Descendant |  |  |  |  |

Retrieve the AOF expression that was used in the call to AdsSetAOF.

Syntax

function AdsGetAOF : String

Description

AdsGetAOF returns the AOF expression string that was used in the call to AdsSetAOF

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

 

eLevel := AdsTable1.AdsEvalAOF( 'LastName = "S" .AND. EMPID > 50' );

{ eLevel equals olPart because EMPID is not indexed }

 

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

strAOF := AdsTable1.AdsGetAOF;

eLevel := AdsTable1.AdsGetAOFOptLevel( strNonOptimizied );

{ eLevel equals olPart because EMPID is not indexed }

{ strNonOptimized equals EMPID>50 }

 

{. . . your code here . . .}

 

AdsTable1.AdsRefreshAOF;

 

See Also

[AdsSetAOF](ade_adssetaof.md)

[AdsRefreshAOF](ade_adsrefreshaof.md)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.md)
