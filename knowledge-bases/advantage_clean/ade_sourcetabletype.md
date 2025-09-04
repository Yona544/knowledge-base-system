---
title: Ade Sourcetabletype
slug: ade_sourcetabletype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sourcetabletype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d69e3fc8b915fb1d4c3524eda56359f25881b828
---

# Ade Sourcetabletype

SourceTableType

TAdsQuery.SourceTableType

Advantage TDataSet Descendant

| TAdsQuery.SourceTableType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Indicates the table/index structure for the table that this component extracts data from.

Syntax

type TAdsTableTypes = (ttAdsCDX, ttAdsVFP, ttAdsADT);

 

property SourceTableType: TAdsTableTypes;

Description

Use SourceTableType to specify the table structure. SourceTableType can be set to either of the following values:

| Value | Meaning |
| ttAdsCDX | Table is a FoxPro compatible table type with CDX/IDX indexes. |
| ttAdsVFP | Table is a Visual FoxPro compatible table type with CDX/IDX indexes. |
| ttAdsADT | (Default) Table is an Advantage proprietary table type with ADI indexes. |

Note The ttAdsNTX file format is not supported on free connections). NTX indexes are supported with TAdsQuery instances on database connections) that use an [Advantage Data Dictionary](master_advantage_data_dictionary.md). Create a new dictionary using the [Advantage Data Architect](ade_advantage_data_architect.md), then reference [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.md) for information on configuring your application to access the dictionary.

 

Note This property is ignored when using a TAdsConnection component that references an [Advantage Data Dictionary](master_advantage_data_dictionary.md). In this situation the table type stored in the dictionary is automatically used.
