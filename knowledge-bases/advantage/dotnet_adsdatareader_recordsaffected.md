AdsDataReader.RecordsAffected




Advantage Database Server 12  

AdsDataReader.RecordsAffected

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.RecordsAffected  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.RecordsAffected Advantage .NET Data Provider dotnet\_Adsdatareader\_recordsaffected Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Properties > AdsDataReader.RecordsAffected / Dear Support Staff, |  |
| AdsDataReader.RecordsAffected  Advantage .NET Data Provider |  |  |  |  |

Gets the number of rows changed, inserted, or deleted by execution of the SQL statement.

public int RecordsAffected { get; }

Remarks

RecordsAffected retrieves the number of rows changed, inserted, or deleted; 0 if no rows were affected or the statement failed; and -1 for SELECT statements.

See Also

[AdsCommand.ExecuteNonQuery](dotnet_adscommand_executenonquery.htm)