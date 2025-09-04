AdsExtendedReader.ProgressMessage




Advantage Database Server 12  

AdsExtendedReader.ProgressMessage

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.ProgressMessage  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.ProgressMessage Advantage .NET Data Provider dotnet\_Adsextendedreader\_progressmessage Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Events > AdsExtendedReader.ProgressMessage / Dear Support Staff, |  |
| AdsExtendedReader.ProgressMessage  Advantage .NET Data Provider |  |  |  |  |

Occurs when Advantage .NET Data Provider receives a progress report from the Advantage Database Server on an index build.

public event AdsInfoMessageEventHandler ProgressMessage;

Remarks

This event provides the ability for an application to register a delegate function to receive progress callbacks during index builds. This can provide equivalent functionality to the AdsExtendedReader.Progress property but does not require a separate thread to monitor the progress. The provider will fire an event each time it receives a progress update from the server, which is generally every 2 seconds.

Note The delegate (event handler) function should not perform any time-consuming tasks when using Advantage Local Server connections. With Advantage Local Server, the event callback is run on the same thread that is executing the index build, which means that the progress is effectively halted until the delegate function returns. If this is an issue, then the AdsExtendedReader.Progress property should be used instead and accessed from a separate thread.

Event Data

The event handler receives an argument of type AdsInfoMessageEventArgs containing data related to this event. The relevant data is the Number property, which contains the estimated percentage of the index build progress.

Example

See [AdsCommand.ProgressMessage](dotnet_adscommand_progressmessage.htm) for an example of how to register a delegate function with the ProgressMessage event.

See Also

[Progress](dotnet_adsextendedreader_progress.htm)

[AdsInfoMessageEventArgs](dotnet_adsinfomessageeventargs.htm)

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[Reindex](dotnet_adsextendedreader_reindex.htm)