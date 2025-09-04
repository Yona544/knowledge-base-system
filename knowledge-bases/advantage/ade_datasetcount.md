DataSetCount




Advantage Database Server 12  

TAdsConnection.DataSetCount

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.DataSetCount  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.DataSetCount Advantage TDataSet Descendant ade\_Datasetcount Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.DataSetCount  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

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

[DataSets](ade_datasets.htm)