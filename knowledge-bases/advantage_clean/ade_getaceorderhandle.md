---
title: Ade Getaceorderhandle
slug: ade_getaceorderhandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getaceorderhandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 339b4b836f3c4671844162fc68e3698953f30ae9
---

# Ade Getaceorderhandle

GetAceOrderHandle

TAdsTable/TAdsQuery.GetAceOrderHandle

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.GetAceOrderHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine index order handle.

Syntax

function GetAceOrderHandle : ADSHANDLE ;

Description

GetAceOrderHandle returns the Advantage Client Engine index handle of the active index. If no index is active, GetAceOrderHandle returns the Advantage Client Engine table or cursor handle. GetAceOrderHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file for examples of how this method is used.

Example

ACE.AdsGotoTop( AdsTable1.GetAceOrderHandle );
