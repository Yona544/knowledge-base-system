---
title: Ade Tabletype
slug: ade_tabletype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tabletype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f80ad92d5292414c90059861a274abdf8c0e3865
---

# Ade Tabletype

TableType

TAdsTable.TableType

Advantage TDataSet Descendant

| TAdsTable.TableType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Indicates the table/index structure for the table that this component encapsulates.

Syntax

type TAdsTableTypes = (ttAdsCDX, ttAdsVFP, ttAdsNTX, ttAdsADT);

 

property TableType: TAdsTableTypes;

Description

Use TableType to specify the table structure. TableType can be set to one of the following values:

| Value | Meaning |
| ttAdsCDX | Table is a FoxPro compatible table type with CDX/IDX indexes |
| ttAdsVFP | Table is a Visual FoxPro compatible table type with CDX/IDX indexes |
| ttAdsNTX | Table is a CA-Clipper compatible table type with NTX indexes |
| ttAdsADT | (Default) Table is an Advantage proprietary table type with ADI indexes. |

Note This property is ignored when using a [TAdsConnection](ade_tadsconnection_7.md) component that references an Advantage Data Dictionary. In this situation the table type stored in the dictionary is automatically used.
