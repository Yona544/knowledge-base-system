---
title: Dotnet Adscommand Commandtimeout
slug: dotnet_adscommand_commandtimeout
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_commandtimeout.htm
source: Advantage CHM
tags:
  - dotnet
checksum: a3d74518ca09c030fe13be9af8915cee113ed865
---

# Dotnet Adscommand Commandtimeout

AdsCommand.CommandTimeout

AdsCommand.CommandTimeout

Advantage .NET Data Provider

| AdsCommand.CommandTimeout  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the wait time before terminating the attempt to execute an SQL statement.

public int CommandTimeout {get; set;}

Remarks

This property value stores the timeout period in seconds for the SQL statement to be run against Advantage Database Server or Advantage Local Server. The default timeout is 30 seconds. A value of 0 indicates that there is no timeout and the command will run indefinitely.

See Also

[AdsCommand.Cancel](dotnet_adscommand_cancel.md)
