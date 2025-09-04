AdsParameter.Direction




Advantage Database Server 12  

AdsParameter.Direction

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter.Direction  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter.Direction Advantage .NET Data Provider dotnet\_Adsparameter\_direction Advantage .NET Data Provider > AdsParameter Class > AdsParameter Properties > AdsParameter.Direction / Dear Support Staff, |  |
| AdsParameter.Direction  Advantage .NET Data Provider |  |  |  |  |

Gets or sets a value indicating whether the parameter is input or output.

public ParameterDirection Direction {get; set;}

Remarks

The Advantage .NET Data Provider currently only supports ParameterDirection.Input and ParameterDirection.Output. Input parameters can be used with SQL statements and stored procedures for sending data to the server. Output parameters can be used with stored procedures. Any AdsParameters with the Direction set to ParameterDirection.Output with names that match the data dictionary definition for stored procedure output parameters will be populated automatically when the stored procedure is executed.

See Also

[AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.htm)