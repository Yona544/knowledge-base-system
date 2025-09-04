AdsCommand.CommandTimeout




Advantage Database Server 12  

AdsCommand.CommandTimeout

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.CommandTimeout  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.CommandTimeout Advantage .NET Data Provider dotnet\_Adscommand\_commandtimeout Advantage .NET Data Provider > AdsCommand Class > AdsCommand Properties > AdsCommand.CommandTimeout / Dear Support Staff, |  |
| AdsCommand.CommandTimeout  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the wait time before terminating the attempt to execute an SQL statement.

public int CommandTimeout {get; set;}

Remarks

This property value stores the timeout period in seconds for the SQL statement to be run against Advantage Database Server or Advantage Local Server. The default timeout is 30 seconds. A value of 0 indicates that there is no timeout and the command will run indefinitely.

See Also

[AdsCommand.Cancel](dotnet_adscommand_cancel.htm)