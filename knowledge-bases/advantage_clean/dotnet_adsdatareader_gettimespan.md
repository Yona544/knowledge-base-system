---
title: Dotnet Adsdatareader Gettimespan
slug: dotnet_adsdatareader_gettimespan
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_gettimespan.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 17316fceff58a455f33676ba9136ed5e5bc11bd2
---

# Dotnet Adsdatareader Gettimespan

AdsDataReader.GetTimeSpan

AdsDataReader.GetTimeSpan

Advantage .NET Data Provider

| AdsDataReader.GetTimeSpan  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a TimeSpan object.

public TimeSpan GetTimeSpan( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a TimeSpan object. No conversions are performed, therefore the data retrieved must already be a time field or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

Note This method can be used to retrieve Advantage Time field values. The System.TimeSpan type is the closest match to the Advantage Time column type.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
