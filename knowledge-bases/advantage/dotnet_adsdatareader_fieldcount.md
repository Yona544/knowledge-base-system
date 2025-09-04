AdsDataReader.FieldCount




Advantage Database Server 12  

AdsDataReader.FieldCount

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.FieldCount  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.FieldCount Advantage .NET Data Provider dotnet\_Adsdatareader\_fieldcount Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Properties > AdsDataReader.FieldCount / Dear Support Staff, |  |
| AdsDataReader.FieldCount  Advantage .NET Data Provider |  |  |  |  |

Gets the number of columns contained in the result set.

public int FieldCount { get; }

Remarks

When not positioned in a valid recordset, this property returns 0; otherwise it returns the number of columns in the result set. The default is -1. After executing a query that does not return rows, FieldCount returns -1.