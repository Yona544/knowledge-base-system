---
title: Ade Refreshparams
slug: ade_refreshparams
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_refreshparams.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9b668068d905d795ddc2a7ad7ad94b9e1898c096
---

# Ade Refreshparams

RefreshParams

TAdsStoredProc.RefreshParams

Advantage TDataSet Descendant

| TAdsStoredProc.RefreshParams  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.md)

Refreshes parameter data stored in TAdsStoredProc.Params

Syntax

property RefreshParams : string;

Description

RefreshParams is a property that can be used at design-time to refresh the information stored in the [TAdsStoredProc.Params](ade_params_tadsstoredproc.md) collection. To force the TAdsStoredProc instance to re-read parameter information from the data dictionary, simply click on the ellipsis in the Object Inspector.

Note Refreshing the parameter data will clear all customizations you may have made to parameters. If customer parameters have been added, or if parameter properties have been modified, it is recommended you make all subsequent modifications manually, and avoid the use of this property.

See Also

[LoadParamsFromDictionary](ade_loadparamsfromdictionary.md)

[Params](ade_params_tadsstoredproc.md)
