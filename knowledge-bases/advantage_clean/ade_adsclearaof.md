---
title: Ade Adsclearaof
slug: ade_adsclearaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclearaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5886fc3b15d8fe4c130328d18bf9114f2ac4fc52
---

# Ade Adsclearaof

AdsClearAOF

TAdsTable.AdsClearAOF

Advantage TDataSet Descendant

| TAdsTable.AdsClearAOF  Advantage TDataSet Descendant |  |  |  |  |

Deactivates the AOF and releases all resources associated with it.

Syntax

procedure AdsClearAOF ;

Description

The AdsClearAOF function deactivates the AOF and releases all resources associated with it on both the client and the server. Note that when a table is closed, any AOF associated with it is automatically cleared as well.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

AdsTable1.First;

{ All rows are filtered where LastName does not begin with S or if EMPID not greater than 50 }

 

{. . . your code here . . .}

 

AdsTable1.AdsClearAOF;

See Also

[AdsSetAOF](ade_adssetaof.md)
