---
title: Ade Adscalcfieldsbeforefilter
slug: ade_adscalcfieldsbeforefilter
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscalcfieldsbeforefilter.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 097ee709b2b9e5eba971a93931e00780c9494163
---

# Ade Adscalcfieldsbeforefilter

AdsCalcFieldsBeforeFilter

TAdsTable.AdsCalcFieldsBeforeFilter

Advantage TDataSet Descendant

| TAdsTable.AdsCalcFieldsBeforeFilter  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Sets when calculated and lookup fields should be populated when using the OnFilterRecord event.

Syntax

property AdsCalcFieldsBeforeFilter: Boolean default False;

Description

This setting specifies when calculated and lookup fields should be populated when using the OnFilterRecord event. The default value is false, which means the overhead of calculating these fields will not happen until after the OnFilterRecord event has been fired. With this behavior, if the record is filtered out you will save the time it would have taken to populate the calculated fields.

If your OnFilterRecord event uses any of your calculated or lookup fields to perform its task, then you should set the AdsCalcFieldsBeforeFilter property to true.
