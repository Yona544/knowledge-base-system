---
title: Dotnet Adsextendedreader Cancel
slug: dotnet_adsextendedreader_cancel
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_cancel.htm
source: Advantage CHM
tags:
  - dotnet
checksum: cb023fc30f11e2ee8655c5f4c218a7802802c80e
---

# Dotnet Adsextendedreader Cancel

AdsExtendedReader.Cancel

AdsExtendedReader.Cancel

Advantage .NET Data Provider

| AdsExtendedReader.Cancel  Advantage .NET Data Provider |  |  |  |  |

Attempts to cancel an index build.

public void Cancel();

Remarks

If an index build is active, the Advantage .NET Data Provider attempts to cancel it when this method is called. No exception is generated if the attempt fails. Please note that if an index build is cancelled, the index file may be left in an unknown and incomplete state. If the index build is cancelled, it will throw an AdsException.

Example

See [AdsCommand.Progress](dotnet_adscommand_progress.md) for an example of how to use the Cancel method.

See Also

[Progress](dotnet_adsextendedreader_progress.md)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.md)

[CreateIndex](dotnet_adsextendedreader_createindex.md)

[Reindex](dotnet_adsextendedreader_reindex.md)
