---
title: Ade Adsevalaof
slug: ade_adsevalaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsevalaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 348020d96ab4b57af96ff4de83115965f8c68f3d
---

# Ade Adsevalaof

AdsEvalAOF

TAdsTable.AdsEvalAOF

Advantage TDataSet Descendant

| TAdsTable.AdsEvalAOF  Advantage TDataSet Descendant |  |  |  |  |

Evaluate a filter expression to determine its optimization level.

Syntax

type TAdsAOFOptimizeLevel = ( olFULL, olPART, olNONE );

 

function AdsEvalAOF ( strFilter : String ): TAdsEvalAOF;

Parameter

| strFilter | Filter expression to evaluate to determine optimization level. |

Description

AdsEvalAOF can be used to determine the optimization level of a potential filter expression. It performs the same parsing as [AdsSetAOF](ade_adssetaof.md) but does not actually build the filter.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

 

eLevel := AdsTable1.AdsEvalAOF( 'LastName = "S" .AND. EMPID > 50' );

{ eLevel equals olPart because EMPID is not indexed }

 

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

eLevel := AdsTable1.AdsGetAOFOptLevel( strNonOptimizied );

{ eLevel equals olPart because EMPID is not indexed }

{ strNonOptimized equals EMPID>50 }

See Also

[AdsSetAOF](ade_adssetaof.md)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.md)
