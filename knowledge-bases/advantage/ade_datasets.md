DataSets




Advantage Database Server 12  

TAdsConnection.DataSets

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.DataSets  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.DataSets Advantage TDataSet Descendant ade\_Datasets Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.DataSets  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

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

[DataSetCount](ade_datasetcount.htm)