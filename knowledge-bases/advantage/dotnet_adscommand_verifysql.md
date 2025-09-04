AdsCommand.VerifySQL




Advantage Database Server 12  

AdsCommand.VerifySQL

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.VerifySQL  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.VerifySQL Advantage .NET Data Provider dotnet\_AdsCommand.VerifySQL Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand.VerifySQL / Dear Support Staff, |  |
| AdsCommand.VerifySQL  Advantage .NET Data Provider |  |  |  |  |

Verifies the given SQL statement is valid.

public void VerifySQL( string strSQL );

Remarks

This method verifies the given statement (strSQL) is a valid SQL statement. The statement is sent to the server where it is parsed but not executed. An exception is raised if the statement is not valid.

See Also

[ExecuteReader](dotnet_adscommand_executereader.htm)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.htm)

[ExecuteScalar](dotnet_adscommand_executescalar.htm)