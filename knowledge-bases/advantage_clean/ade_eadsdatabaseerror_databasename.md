---
title: Ade Eadsdatabaseerror Databasename
slug: ade_eadsdatabaseerror_databasename
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_databasename.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a54cc5553678a4e1246378c52d54b9d81643b642
---

# Ade Eadsdatabaseerror Databasename

EADSDatabaseError.DatabaseName

EADSDatabaseError.DatabaseName

Advantage TDataSet Descendant

| EADSDatabaseError.DatabaseName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

The DatabaseName property associated with the dataset that raised the exception.

Syntax

property DatabaseName : STRING;

Description

DatabaseName contains the DatabaseName property of the dataset that raised the exception (e.g., DBDEMO). This string is equivalent to the TAdsDataSet.DatabaseName property assigned to the dataset that raised the exception.

If the DatabaseName property of the dataset is an alias or TAdsConnection object and path information is desired utilize the [DatabasePath](ade_eadsdatabaseerror_databasepath.md) property.

If the dataset was not available to the method raising the exception the DatabaseName property will contain an empty string.
