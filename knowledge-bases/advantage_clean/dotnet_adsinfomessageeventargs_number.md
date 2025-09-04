---
title: Dotnet Adsinfomessageeventargs Number
slug: dotnet_adsinfomessageeventargs_number
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsinfomessageeventargs_number.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3d8c907eb638bddec5fd40608e19476ff17cbd2a
---

# Dotnet Adsinfomessageeventargs Number

AdsInfoMessageEventArgs.Number

AdsInfoMessageEventArgs.Number

Advantage .NET Data Provider

| AdsInfoMessageEventArgs.Number  Advantage .NET Data Provider |  |  |  |  |

Gets the native Advantage error/warning number associated with the warning event. If it is used in conjunction with AdsCommand.ProgressMessage or AdsExtendedReader.ProgressMessage, then this number represents the integer percentage of the progress (0 to 100).

public int Number { get; }
