---
title: Ade Adsgetaofoptlevel
slug: ade_adsgetaofoptlevel
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetaofoptlevel.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 13a23c4ecdfdee35cddd6e419a50db45ec9f73cb
---

# Ade Adsgetaofoptlevel

AdsGetAOFOptLevel

TAdsTable/TAdsQuery.AdsGetAOFOptLevel

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsGetAOFOptLevel  Advantage TDataSet Descendant |  |  |  |  |

Return the optimization level of the Advantage Optimized Filter.

Syntax

type TAdsAOFOptimizeLevel = (olFULL, olPART, olNONE);

 

function AdsGetAOFOptLevel ( var strFilter : String ) : TAdsAOFOtimizeLevel

Parameter

| strFilter | The AOF filter to check. Return the non-optimized portion of the filter expression in this buffer. This parameter can be an empty string if only the optimization level is desired. |

Description

AdsGetAOFOptLevel returns the optimization level of the AOF expression associated with the given handle. It also returns the portion of the expression that could not be optimized. For example, if a table has a single index built on 'LASTNAME', the filter expression "LASTNAME = 'James' .and. FIRSTNAME = 'Bob'" will be partially optimized. AdsGetAOFOptLevel would return ADS\_OPTIMIZED\_PART for this expression, and the non-optimized portion would be "FIRSTNAME='Bob'".

Filters created on datasets opened with the ADS\_NTX option will not be optimized; only filters created on ADS\_CDX, ADS\_VFP, or ADS\_ADT datasets will be optimized. See [Advantage Optimized Filters](master_advantage_optimized_filters.md) for more information.

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

[AdsRefreshAOF](ade_adsrefreshaof.md)

[AdsGetAOF](ade_adsgetaof.md)
