---
title: Dotnet Adsextendedreader Relativekeyposition
slug: dotnet_adsextendedreader_relativekeyposition
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_relativekeyposition.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d0b8d795260a8cc00fde84e2c91505b52adeb262
---

# Dotnet Adsextendedreader Relativekeyposition

AdsExtendedReader.RelativeKeyPosition

AdsExtendedReader.RelativeKeyPosition

Advantage .NET Data Provider

| AdsExtendedReader.RelativeKeyPosition  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the relative position of the current record in the index order.

public double RelativeKeyPosition{ get; set; }

Remarks

RelativeKeyPosition gets or sets the approximate the position in the index order between 0.0 and 1.0. If there is a scope set, RelativeKeyPosition calculates the position relative to the current scope.

Note Setting RelativeKeyPosition will throw an exception if active handle is not an index handle.
