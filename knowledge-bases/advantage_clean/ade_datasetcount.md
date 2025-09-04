---
title: Ade Datasetcount
slug: ade_datasetcount
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_datasetcount.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 92b673f1d5bf3c9d9abf450f228974a19756d2df
---

# Ade Datasetcount

DataSetCount

TAdsConnection.DataSetCount

Advantage TDataSet Descendant

| TAdsConnection.DataSetCount  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Indicates the number of datasets associated with the connection component.

Syntax

property DataSetCount: Integer

Description

Use DataSetCount to determine the number of datasets listed by the DataSets property. DataSets lists all associated datasets, regardless of whether or not they are active.

Use DataSetCount as an upper bound when iterating through the DataSets property.

Example

with AdsConnection1 do

begin

for i := 0 to (DataSetCount-1) do

if ( DataSets[i].Active = TRUE ) then

DataSets[i].First;

end;

See Also

[DataSets](ade_datasets.md)
