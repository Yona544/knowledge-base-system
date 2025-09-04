---
title: Ade Loadparamsfromdictionary
slug: ade_loadparamsfromdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_loadparamsfromdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 72bd45f966acb57ec21867889315bcd39e90a385
---

# Ade Loadparamsfromdictionary

LoadParamsFromDictionary

TAdsStoredProc.LoadParamsFromDictionary

Advantage TDataSet Descendant

| TAdsStoredProc.LoadParamsFromDictionary  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.md)

Reads parameter information from the Advantage Data Dictionary.

Syntax

procedure LoadParamsFromDictionary;

Description

LoadParamsFromDictionary populates the [Params](ade_params_tadsstoredproc.md) property with the parameter information associated with the procedure in the Advantage Data Dictionary. If the StoredProcName property is assigned when the TAdsStoredProc is attached to an open TAdsConnection component (for example, at design-time) this procedure is called automatically.

Use this procedure if you are configuring a new TAdsStoredProc instance at run-time, and would like to have the Params property automatically populated, as opposed to writing the code to configure the parameters.
