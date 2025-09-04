---
title: Dotnet Adsextendedreader Setint16
slug: dotnet_adsextendedreader_setint16
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setint16.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1e4599116a24fe2a58ec1297f96cb07e98dd644c
---

# Dotnet Adsextendedreader Setint16

AdsExtendedReader.SetInt16

AdsExtendedReader.SetInt16

Advantage .NET Data Provider

| AdsExtendedReader.SetInt16  Advantage .NET Data Provider |  |  |  |  |

Stores the given Int16 value in the specified column.

public void SetInt16( int iCol, Int16 value );

Remarks

This method sets the specified zero-based column 16-bit signed integer value to the given Int16 value. No conversions are performed. To set an integer field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetInt16](dotnet_adsdatareader_getint16.md)
