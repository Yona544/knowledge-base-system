---
title: Dotnet Adscommand Timedout
slug: dotnet_adscommand_timedout
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_timedout.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 131f7df6949ac1f4c9ff4acc2889b2480945888a
---

# Dotnet Adscommand Timedout

AdsCommand.TimedOut

AdsCommand.TimedOut

Advantage .NET Data Provider

| AdsCommand.TimedOut  Advantage .NET Data Provider |  |  |  |  |

Indicates whether a command was cancelled because it exceeded the [AdsCommand.CommandTimeout](dotnet_adscommand_commandtimeout.md) limit.

public bool TimedOut {get;}

Remarks

This property returns True if the SQL command was cancelled by the Advantage .NET Data Provider because it exceeded the limit in the [AdsCommand.CommandTimeout](dotnet_adscommand_commandtimeout.md) property.

See Also

[CommandTimeout](dotnet_adscommand_commandtimeout.md)

[Cancelled](dotnet_adscommand_cancelled.md)

[Cancel](dotnet_adscommand_cancel.md)
