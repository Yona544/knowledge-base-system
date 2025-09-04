MasterFields




Advantage Database Server 12  

TAdsTable/TAdsQuery.MasterFields

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.MasterFields  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.MasterFields Advantage TDataSet Descendant ade\_Masterfields Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.MasterFields  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Specifies fields in the master dataset to link with corresponding fields in this dataset in order to establish a master-detail relationship between the datasets.

Syntax

property MasterFields: string;

Description

Use MasterFields after setting the MasterSource property to specify the name of the fields to use in establishing a detail-master relationship between this dataset and the one specified in MasterSource. MasterFields is a string containing a semi-colon delimited list of field names in the master dataset. Each field in the list must correspond to a field in the IndexFieldNames property. The corresponding fields must be of the exact size and type. If the MasterFields property contains less field names than the IndexFieldNames propery, then only the fields listed will be used to select records in the Detail dataset. Note that the IndexFieldNames property does not actually have to be filled in because the IndexName property is equivalent and mutually exclusive.

Each time the current record in the master dataset changes, the new values in that field are used to select corresponding records in this dataset for display.

Note Advantage does not provide a Field Link Designer like the one available with TTable.