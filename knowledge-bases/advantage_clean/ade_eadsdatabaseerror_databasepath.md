---
title: Ade Eadsdatabaseerror Databasepath
slug: ade_eadsdatabaseerror_databasepath
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_databasepath.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 82ea324c5ddc22151b1d7112236245010ae7ac37
---

# Ade Eadsdatabaseerror Databasepath

EADSDatabaseError.DatabasePath

EADSDatabaseError.DatabasePath

Advantage TDataSet Descendant

| EADSDatabaseError.DatabasePath  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

Path to the table/connection associated with the dataset that raised the exception.

Syntax

property DatabasePath : STRING;

Description

DatabasePath contains the path to the table/connection that raised the exception. If the datasets DatabaseName property is a path this property is equivalent to the EADSDatabaseError.DatabaseName property. If the datasets DatabaseName property is either an alias or a TAdsConnection object this property will be the path associated with the alias or TAdsConnection.

If the dataset was not available to the method raising the exception the DatabasePath property will contain an empty string.
