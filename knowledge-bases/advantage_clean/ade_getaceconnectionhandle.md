---
title: Ade Getaceconnectionhandle
slug: ade_getaceconnectionhandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getaceconnectionhandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d75be1d8dd1209c2f94303f8b9d3f5277f0d2bf2
---

# Ade Getaceconnectionhandle

GetAceConnectionHandle

TAdsTable/TAdsQuery.GetAceConnectionHandle

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.GetAceConnectionHandle  Advantage TDataSet Descendant |  |  |  |  |

Returns the Advantage Client Engine connection handle.

Syntax

function GetAceConnectionHandle : ADSHANDLE ;

Description

GetAceConnectionHandle returns the active connection handle, which is the connection handle being used by the specified dataset instance. If no table or cursor is open or no connection exists, the Advantage Client Engine connection handle returned will not be valid. GetAceConnectionHandle is only useful if you are going to call Advantage Client Engine functionality directly that is prototyped in ACE.PAS. Please refer to the ADSFUNC.PAS source file to see examples of how this method is used.

Example

ACE.AdsBeginTransaction( AdsTable1.GetAceConnectionHandle );
