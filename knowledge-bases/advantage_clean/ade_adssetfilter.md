---
title: Ade Adssetfilter
slug: ade_adssetfilter
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetfilter.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: aba80b6c68fc066b750e398d5c0e1168175a226c
---

# Ade Adssetfilter

AdsSetFilter

TAdsTable.AdsSetFilter

Advantage TDataSet Descendant

| TAdsTable.AdsSetFilter  Advantage TDataSet Descendant |  |  |  |  |

Sets a filter on the given table.

Syntax

procedure AdsSetFilter( strFilter : String );

Parameter

| strFilter | Expression given as a pascal-style string. If there is an existing filter on the given table, it is replaced with the new filter. This affects subsequent record movements other than AdsGotoRecord. |

Description

Setting a filter through AdsSetFilter allows only the records that pass the filter expression to be visible. The filter expression must result in a boolean True or False. After setting a filter, the table may still be positioned on a record that does not pass the filter. To activate the filter, perform an AdsGotoTop or some other movement function.

See [Advantage Expression Engine](master_advantage_expression_engine.md) for a list of functions supported by Advantage Expression Engine.

Note AdsSetFilter does not utilize the Advantage Optimized Filters functionality. It is recommended you use the native Delphi properties (Filter and Filtered) to set a filter. If you must use an Advantage specific API, the [AdsSetAOF](ade_adssetaof.md) function is recommended.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetFilter( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

strFilter := AdsTable1.AdsGetFilter;

See Also

[AdsClearFilter](ade_adsclearfilter.md)

[AdsGetFilter](ade_adsgetfilter.md)
