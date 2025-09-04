---
title: Ade Datasets
slug: ade_datasets
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_datasets.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9721f4216c72c19e19c2c11190886f3f5ad23fbf
---

# Ade Datasets

DataSets

TAdsConnection.DataSets

Advantage TDataSet Descendant

| TAdsConnection.DataSets  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Lists the datasets currently using this connection component.

Syntax

property DataSets[Index: Integer]: TDataSet

Description

Use DataSets to access the datasets that are currently using the connection component. DataSets lists all associated datasets, regardless of whether or not they are active.

Use DataSetCount as an upper bound when iterating through the DataSets property.

Example

with AdsConnection1 do

begin

for i := 0 to (DataSetCount-1) do

if ( DataSets[i].Active = TRUE ) then

DataSets[i].First;

end;

See Also

[DataSetCount](ade_datasetcount.md)
