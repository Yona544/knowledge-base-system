---
title: Dotnet Adscommand Cancel
slug: dotnet_adscommand_cancel
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_cancel.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5aaba546d8aef64692c5025fa7a45c6965ba1c28
---

# Dotnet Adscommand Cancel

AdsCommand.Cancel

AdsCommand.Cancel

Advantage .NET Data Provider

| AdsCommand.Cancel  Advantage .NET Data Provider |  |  |  |  |

Attempts to cancel the execution of an SQL statement.

public void Cancel();

Remarks

If an SQL statement is executing, the Advantage .NET Data Provider attempts to cancel it when this method is called. No exception is generated if the attempt fails.

Example

See [AdsCommand.Progress](dotnet_adscommand_progress.md) for an example.

See Also

[Cancelled](dotnet_adscommand_cancelled.md)

[CommandTimeout](dotnet_adscommand_commandtimeout.md)

[TimedOut](dotnet_adscommand_timedout.md)

[ProgressMessage](dotnet_adscommand_progressmessage.md)
