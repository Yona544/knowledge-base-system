AdsDataAdapter.FillSchema




Advantage Database Server 12  

AdsDataAdapter.FillSchema

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter.FillSchema  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter.FillSchema Advantage .NET Data Provider dotnet\_Adsdataadapter\_fillschema Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Methods > AdsDataAdapter.FillSchema / Dear Support Staff, |  |
| AdsDataAdapter.FillSchema  Advantage .NET Data Provider |  |  |  |  |

Adds a DataTable to a DataSet and configures the schema to match that in the data source.

The following overloaded versions are supported:

public override DataTable[] FillSchema( DataSet dataSet, SchemaType schemaType );

 

public DataTable FillSchema( DataTable dataTable, SchemaType schemaType );

 

public DataTable[] FillSchema( DataSet dataSet, SchemaType schemaType, string srcTable );

Remarks

The return value is a reference to a collection of DataTable objects that were added to the DataSet. This method retrieves the schema information from the data source using the [AdsDataAdapter.SelectCommand](dotnet_adsdataadapter_selectcommand.htm).

See Also

[GetSchemaTable](dotnet_adsdatareader_getschematable.htm)