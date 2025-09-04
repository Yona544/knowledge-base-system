AdsExtendedReader.Progress




Advantage Database Server 12  

AdsExtendedReader.Progress

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.Progress  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.Progress Advantage .NET Data Provider dotnet\_Adsextendedreader\_progress Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.Progress / Dear Support Staff, |  |
| AdsExtendedReader.Progress  Advantage .NET Data Provider |  |  |  |  |

Gets the current progress of a current index build.

public int Progress {get;}

Remarks

This retrieves the current progress estimate of an index build initiated by a call to Reindex or CreateIndex. It can be retrieved by another thread to provide some kind of visual feedback (e.g., a progress bar). The value returned will range from 0 to 100.

Example

See [AdsCommand.Progress](dotnet_adscommand_progress.htm) for an example of how to use the progress property of an object.

See Also

[Cancel](dotnet_adsextendedreader_cancel.htm)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.htm)

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[Reindex](dotnet_adsextendedreader_reindex.htm)