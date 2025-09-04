---
title: Ade Adsclearfilter
slug: ade_adsclearfilter
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclearfilter.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7f575d1f60c1636727cf91839b5ba22b14198e78
---

# Ade Adsclearfilter

AdsClearFilter

TAdsTable.AdsClearFilter

Advantage TDataSet Descendant

| TAdsTable.AdsClearFilter  Advantage TDataSet Descendant |  |  |  |  |

Clears the current filter expression in a given table.

Syntax

procedure AdsClearFilter;

Description

AdsClearFilter will remove the current filter from the specified table, allowing records that previously had not passed the filter to become visible again.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetFilter( 'LastName = "S" .AND. EMPID > 50' );

AdsTable1.First;

{ The row is filtered if LastName does not begin with S or if EMPID not greater than 50 }

{. . . your code here . . .}

 

AdsTable1.AdsClearFilter;

See Also

[AdsGetFilter](ade_adsgetfilter.md)

[AdsSetFilter](ade_adssetfilter.md)
