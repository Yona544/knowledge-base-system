AdsCommand.Cancel




Advantage Database Server 12  

AdsCommand.Cancel

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.Cancel  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.Cancel Advantage .NET Data Provider dotnet\_Adscommand\_cancel Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand.Cancel / Dear Support Staff, |  |
| AdsCommand.Cancel  Advantage .NET Data Provider |  |  |  |  |

Attempts to cancel the execution of an SQL statement.

public void Cancel();

Remarks

If an SQL statement is executing, the Advantage .NET Data Provider attempts to cancel it when this method is called. No exception is generated if the attempt fails.

Example

See [AdsCommand.Progress](dotnet_adscommand_progress.htm) for an example.

See Also

[Cancelled](dotnet_adscommand_cancelled.htm)

[CommandTimeout](dotnet_adscommand_commandtimeout.htm)

[TimedOut](dotnet_adscommand_timedout.htm)

[ProgressMessage](dotnet_adscommand_progressmessage.htm)