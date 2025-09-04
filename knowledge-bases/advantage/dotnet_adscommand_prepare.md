AdsCommand.Prepare




Advantage Database Server 12  

AdsCommand.Prepare

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.Prepare  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.Prepare Advantage .NET Data Provider dotnet\_Adscommand\_prepare Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand.Prepare / Dear Support Staff, |  |
| AdsCommand.Prepare  Advantage .NET Data Provider |  |  |  |  |

Performs the initial preparation of the statement specified in [AdsCommand.CommandText](dotnet_adscommand_commandtext.htm).

public void Prepare();

Remarks

This method prepares the statement for execution on the server. It is generally not necessary to call this method because it is called automatically by Advantage .NET Data Provider when methods such as [AdsCommand.ExecuteReader](dotnet_adscommand_executereader.htm) and [AdsCommand.ExecuteNonQuery](dotnet_adscommand_executenonquery.htm) are called. There is no efficiency gain by calling this method first.

If you do call this method and [AdsCommand.CommandType](dotnet_adscommand_commandtype.htm) is set to CommandType.StoredProcedure, you must have set up the parameters for the stored procedure first.

See Also

[ExecuteReader](dotnet_adscommand_executereader.htm)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.htm)

[ExecuteScalar](dotnet_adscommand_executescalar.htm)

[DeriveParameters](dotnet_adscommand_deriveparameters.htm)