---
title: Ade Getaceindexhandle
slug: ade_getaceindexhandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getaceindexhandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9e7119d8227cf8625d983dbd3890943aac3f6680
---

# Ade Getaceindexhandle

GetAceIndexHandle

TAdsTable/TAdsQuery.GetAceIndexHandle

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.GetAceIndexHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine index handle.

Syntax

function GetAceIndexHandle : ADSHANDLE ;

Description

GetAceIndexHandle returns the current Advantage Client Engine index handle. If no index is active, then 0 is returned. GetAceIndexHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file for examples of how this method is used.

Example

ACE.AdsGotoTop( AdsTable1.GetAceIndexHandle );
