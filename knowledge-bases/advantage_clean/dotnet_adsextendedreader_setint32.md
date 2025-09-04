---
title: Dotnet Adsextendedreader Setint32
slug: dotnet_adsextendedreader_setint32
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setint32.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 53b99d50b0158861e29787261ec025575547311f
---

# Dotnet Adsextendedreader Setint32

AdsExtendedReader.SetInt32

AdsExtendedReader.SetInt32

Advantage .NET Data Provider

| AdsExtendedReader.SetInt32  Advantage .NET Data Provider |  |  |  |  |

Stores the given Int32 value in the specified column.

public void SetInt32( int iCol, Int32 value );

Remarks

This method sets the specified zero-based column 32-bit signed integer value to the given Int32 value. No conversions are performed. To set an integer field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetInt32](dotnet_adsdatareader_getint32.md)
