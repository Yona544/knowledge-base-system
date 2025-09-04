---
title: Dotnet Adscommand Cancelled
slug: dotnet_adscommand_cancelled
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_cancelled.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 55877043ef23e712e184a61dcb17947115d70a0c
---

# Dotnet Adscommand Cancelled

AdsCommand.Cancelled

AdsCommand.Cancelled

Advantage .NET Data Provider

| AdsCommand.Cancelled  Advantage .NET Data Provider |  |  |  |  |

Indicates if a command was cancelled by a call to [AdsCommand.Cancel](dotnet_adscommand_cancel.md).

public bool Cancelled {get;}

Remarks

This property returns True if the SQL command was cancelled by the Advantage .NET Data Provider because the [AdsCommand.Cancel](dotnet_adscommand_cancel.md) method was called.

See Also

[AdsCommand.CommandTimeout](dotnet_adscommand_commandtimeout.md)

[AdsCommand.TimedOut](dotnet_adscommand_timedout.md)

[AdsCommand.Cancel](dotnet_adscommand_cancel.md)
