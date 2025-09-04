---
title: Ade Adsgethandletype
slug: ade_adsgethandletype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgethandletype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 83678da44da8b25525bb69e0394c757fab4c2fb5
---

# Ade Adsgethandletype

AdsGetHandleType

TAdsTable.AdsGetHandleType

Advantage TDataSet Descendant

| TAdsTable.AdsGetHandleType  Advantage TDataSet Descendant |  |  |  |  |

Returns the type of a given Advantage Client Engine handle.

Syntax

type TAdsHandleTypes = ( htTABLE, htINDEX );

 

function AdsGetHandleType( hObj : ADSHANDLE ) : TAdsHandleTypes;

Parameter

| hObj | Handle of either a table or an index order. |

Description

Possible types returned are htTABLE for table handles and htINDEX for index order handles.

Example

AdsTable1.Active := TRUE;

eAdsHandleType := AdsTable1.AdsGetHandleType( AdsTable1.GetAceOrderHandle );

See Also

[AdsGetIndexHandle](ade_adsgetindexhandle.md)

[AdsGetIndexHandleByOrder](ade_adsgetindexhandlebyorder.md)
