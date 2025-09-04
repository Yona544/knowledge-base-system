---
title: Ade Getprocedurenames
slug: ade_getprocedurenames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getprocedurenames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7be32f76db1088f4378f5a18c82172fb3f66d013
---

# Ade Getprocedurenames

GetProcedureNames

TAdsConnection.GetProcedureNames

Advantage TDataSet Descendant

| TAdsConnection.GetProcedureNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Retrieves a list of stored procedures from an Advantage Data Dictionary.

Syntax

procedure GetProcedureNames( poList : TStrings );

Description

GetProcedureNames retrieves a list of Advantage Extended Procedures from the Advantage Data Dictionary referenced by the TAdsConnection component. If the TAdsConnection component does not reference an Advantage Data Dictionary the procedure returns without modifying the list. See [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.md) for more details on associating a TAdsConnection component with an Advantage Data Dictionary.
