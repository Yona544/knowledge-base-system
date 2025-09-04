---
title: Dotnet Adsextendedreader Setint64
slug: dotnet_adsextendedreader_setint64
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setint64.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0fb164a8eb5295831899313315b2890806d959dc
---

# Dotnet Adsextendedreader Setint64

AdsExtendedReader.SetInt64

AdsExtendedReader.SetInt64

Advantage .NET Data Provider

| AdsExtendedReader.SetInt64  Advantage .NET Data Provider |  |  |  |  |

Stores the given Int64 value in the specified column.

public void SetInt64( int iCol, Int64 value );

Remarks

This method sets the specified zero-based column 64-bit signed integer value to the given Int64 value. No conversions are performed. To set an integer field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetInt64](dotnet_adsdatareader_getint64.md)
