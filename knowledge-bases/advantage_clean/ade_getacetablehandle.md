---
title: Ade Getacetablehandle
slug: ade_getacetablehandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getacetablehandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: cc159fba1c675ccc412fc8195fc995e5beb7276e
---

# Ade Getacetablehandle

GetAceTableHandle

TAdsTable/TAdsQuery.GetAceTableHandle

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.GetAceTableHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine table or cursor handle.

Syntax

function GetAceTableHandle : ADSHANDLE ;

Description

GetAceTableHandle returns the current open table or cursor handle. If the table or cursor is closed, the Advantage Client Engine handle returned will not be valid. GetAceTableHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file for examples of how this method is used.

Example

ACE.AdsGotoTop( AdsTable1.GetAceTableHandle );
