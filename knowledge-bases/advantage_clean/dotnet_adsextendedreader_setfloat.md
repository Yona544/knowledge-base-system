---
title: Dotnet Adsextendedreader Setfloat
slug: dotnet_adsextendedreader_setfloat
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setfloat.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 43810ce7deaaecd4857c53dcd6e9145de52da556
---

# Dotnet Adsextendedreader Setfloat

AdsExtendedReader.SetFloat

AdsExtendedReader.SetFloat

Advantage .NET Data Provider

| AdsExtendedReader.SetFloat  Advantage .NET Data Provider |  |  |  |  |

Stores the given float value in the specified column.

public void SetFloat( int iCol, float value );

Remarks

This method sets the specified zero-based column single-precision floating-point value to the given float value. No conversions are performed. To set a float field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetFloat](dotnet_adsdatareader_getfloat.md)
