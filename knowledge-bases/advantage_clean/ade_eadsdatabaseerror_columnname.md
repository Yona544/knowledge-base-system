---
title: Ade Eadsdatabaseerror Columnname
slug: ade_eadsdatabaseerror_columnname
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_columnname.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d562598cedfb9e7bdb54fd903d3516dc92d8f55c
---

# Ade Eadsdatabaseerror Columnname

EADSDatabaseError.ColumnName

EADSDatabaseError.ColumnName

Advantage TDataSet Descendant

| EADSDatabaseError.ColumnName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

The column name associated with a constraint error.

Syntax

property ColumnName : STRING;

Description

ColumnName contains the name of the offending field when the error raised is a constraint error.

Note If a custom validation message has been assigned, this property will be populated only if the column name appears as the first quoted string after the word column. For example, 'this is a custom message for column "lastname"' would correctly populate this property with the value "lastname".
