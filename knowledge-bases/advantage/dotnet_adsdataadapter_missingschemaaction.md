AdsDataAdapter.MissingSchemaAction




Advantage Database Server 12  

AdsDataAdapter.MissingSchemaAction

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter.MissingSchemaAction  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter.MissingSchemaAction Advantage .NET Data Provider dotnet\_Adsdataadapter\_missingschemaaction Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Properties > AdsDataAdapter.MissingSchemaAction / Dear Support Staff, |  |
| AdsDataAdapter.MissingSchemaAction  Advantage .NET Data Provider |  |  |  |  |

Indicates or specifies whether missing source tables, columns, and their relationships are added to the data set schema, ignored, or cause an error to be raised.

public MissingSchemaAction MissingSchemaAction {get; set;}

Remarks

The following table shows the valid values. The default is Add.

|  |  |
| --- | --- |
| Member Name | Description |
| Add | Adds the necessary columns to complete the schema. |
| AddWithKey | Adds the necessary columns and primary key information to complete the schema. |
| Error | A SystemException is generated. |
| Ignore | Ignores the extra columns. |