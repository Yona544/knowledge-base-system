AdsCommand.Connection




Advantage Database Server 12  

AdsCommand.Connection

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.Connection  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.Connection Advantage .NET Data Provider dotnet\_Adscommand\_connection Advantage .NET Data Provider > AdsCommand Class > AdsCommand Properties > AdsCommand.Connection / Dear Support Staff, |  |
| AdsCommand.Connection  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the [AdsConnection](dotnet_adsconnection.htm) used by this instance of the AdsCommand

public AdsConnection Connection {get; set;}

Remarks

If you set Connection while the command object has an open reader, AdsCommand will throw an InvalidOperationException.

See Also

[AdsConnection](dotnet_adsconnection.htm)