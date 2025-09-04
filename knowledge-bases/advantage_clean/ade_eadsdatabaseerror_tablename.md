---
title: Ade Eadsdatabaseerror Tablename
slug: ade_eadsdatabaseerror_tablename
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_tablename.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3a7b69d23bae77c61f885f7f33e8c4e36414a2e1
---

# Ade Eadsdatabaseerror Tablename

EADSDatabaseError.TableName

EADSDatabaseError.TableName

Advantage TDataSet Descendant

| EADSDatabaseError.TableName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

The TableName property associated with the dataset that raised the exception.

Syntax

property TableName : STRING;

Description

TableName contains the TableName property of the dataset that raised the exception (e.g., demotable.adt). This string is equivalent to the TAdsDataSet.TableName property assigned to the dataset that raised the exception.

If the dataset was not available to the method raising the exception the TableName property will contain an empty string.

Note When using TAdsQuery this property will always contain an empty string.
