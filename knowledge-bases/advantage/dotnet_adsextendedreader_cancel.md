AdsExtendedReader.Cancel




Advantage Database Server 12  

AdsExtendedReader.Cancel

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.Cancel  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.Cancel Advantage .NET Data Provider dotnet\_Adsextendedreader\_cancel Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.Cancel / Dear Support Staff, |  |
| AdsExtendedReader.Cancel  Advantage .NET Data Provider |  |  |  |  |

Attempts to cancel an index build.

public void Cancel();

Remarks

If an index build is active, the Advantage .NET Data Provider attempts to cancel it when this method is called. No exception is generated if the attempt fails. Please note that if an index build is cancelled, the index file may be left in an unknown and incomplete state. If the index build is cancelled, it will throw an AdsException.

Example

See [AdsCommand.Progress](dotnet_adscommand_progress.htm) for an example of how to use the Cancel method.

See Also

[Progress](dotnet_adsextendedreader_progress.htm)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.htm)

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[Reindex](dotnet_adsextendedreader_reindex.htm)