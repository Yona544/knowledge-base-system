---
title: Ade Adsgetfilter
slug: ade_adsgetfilter
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetfilter.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a1460069c7d9a591557d678c0ba3469f16e0d2f9
---

# Ade Adsgetfilter

AdsGetFilter

TAdsTable.AdsGetFilter

Advantage TDataSet Descendant

| TAdsTable.AdsGetFilter  Advantage TDataSet Descendant |  |  |  |  |

Returns the current filter expression for the given table.

Syntax

function AdsGetFilter : String;

Description

AdsGetFilter returns the current filter expression for the specified table. Note that the case of the expression returned is not guaranteed to be identical to the filter expression that was set.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetFilter( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

strFilter := AdsTable1.AdsGetFilter;

See Also

[AdsClearFilter](ade_adsclearfilter.md)

[AdsSetFilter](ade_adssetfilter.md)
