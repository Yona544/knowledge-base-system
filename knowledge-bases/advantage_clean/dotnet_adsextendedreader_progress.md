---
title: Dotnet Adsextendedreader Progress
slug: dotnet_adsextendedreader_progress
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_progress.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 985f69d5f31ad03525f5c043ecc29bb15138298b
---

# Dotnet Adsextendedreader Progress

AdsExtendedReader.Progress

AdsExtendedReader.Progress

Advantage .NET Data Provider

| AdsExtendedReader.Progress  Advantage .NET Data Provider |  |  |  |  |

Gets the current progress of a current index build.

public int Progress {get;}

Remarks

This retrieves the current progress estimate of an index build initiated by a call to Reindex or CreateIndex. It can be retrieved by another thread to provide some kind of visual feedback (e.g., a progress bar). The value returned will range from 0 to 100.

Example

See [AdsCommand.Progress](dotnet_adscommand_progress.md) for an example of how to use the progress property of an object.

See Also

[Cancel](dotnet_adsextendedreader_cancel.md)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.md)

[CreateIndex](dotnet_adsextendedreader_createindex.md)

[Reindex](dotnet_adsextendedreader_reindex.md)
