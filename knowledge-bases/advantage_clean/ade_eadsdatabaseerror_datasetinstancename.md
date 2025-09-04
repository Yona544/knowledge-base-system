---
title: Ade Eadsdatabaseerror Datasetinstancename
slug: ade_eadsdatabaseerror_datasetinstancename
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_datasetinstancename.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 44a99466b6417500ecf0fb8c5dad119c95febdbe
---

# Ade Eadsdatabaseerror Datasetinstancename

EADSDatabaseError.DataSetInstanceName

EADSDatabaseError.DataSetInstanceName

Advantage TDataSet Descendant

| EADSDatabaseError.DataSetInstanceName  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

The name of the dataset that raised the exception.

Syntax

property DataSetInstanceName : STRING;

Description

DataSetInstanceName contains a string representation of the name of the dataset that raised the exception (e.g., AdsTable1). This string is equivalent to the TAdsDataSet.Name property assigned to the dataset that raised the exception.

If the name of the dataset was not available to the method raising the exception the DataSetInstanceName property will contain an empty string.
