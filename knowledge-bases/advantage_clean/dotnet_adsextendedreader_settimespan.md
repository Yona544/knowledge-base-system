---
title: Dotnet Adsextendedreader Settimespan
slug: dotnet_adsextendedreader_settimespan
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_settimespan.htm
source: Advantage CHM
tags:
  - dotnet
checksum: da832e366e1bbc4454922ed0a14b9e9e0ce283f3
---

# Dotnet Adsextendedreader Settimespan

AdsExtendedReader.SetTimeSpan

AdsExtendedReader.SetTimeSpan

Advantage .NET Data Provider

| AdsExtendedReader.SetTimeSpan  Advantage .NET Data Provider |  |  |  |  |

Stores the given TimeSpan value in the specified column.

public void SetTimeSpan( int iCol, TimeSpan value);

Remarks

This method sets the specified zero-based column value to the given TimeSpan value. No conversions are performed. To set a TimeSpan field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetTimeSpan](dotnet_adsdatareader_gettimespan.md)
