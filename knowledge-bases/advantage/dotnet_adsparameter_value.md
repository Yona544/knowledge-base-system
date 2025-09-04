AdsParameter.Value




Advantage Database Server 12  

AdsParameter.Value

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter.Value  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter.Value Advantage .NET Data Provider dotnet\_Adsparameter\_value Advantage .NET Data Provider > AdsParameter Class > AdsParameter Properties > AdsParameter.Value / Dear Support Staff, |  |
| AdsParameter.Value  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the value of the parameter.

public object Value {get; set;}

Remarks

The default value is null. For input parameters, the value is bound to the AdsCommand that is sent to the server. For output value parameters, the value is set after any successful execution of the command.

Null parameter values can be specified by setting the Value property to null or DBNull.Value.

When the value is set, the [AdsParameter.DbType](dotnet_adsparameter_dbtype.htm) is inferred from the value if the type has not already been explicitly assigned.

See Also

[DbType](dotnet_adsparameter_dbtype.htm)