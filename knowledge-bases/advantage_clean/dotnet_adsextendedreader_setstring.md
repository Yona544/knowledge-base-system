---
title: Dotnet Adsextendedreader Setstring
slug: dotnet_adsextendedreader_setstring
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setstring.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8f3beb0395eca772b7cb5ce173e46d85248f987a
---

# Dotnet Adsextendedreader Setstring

AdsExtendedReader.SetString

AdsExtendedReader.SetString

Advantage .NET Data Provider

| AdsExtendedReader.SetString  Advantage .NET Data Provider |  |  |  |  |

Stores the given string value in the specified column.

public void SetString( int iCol, string value );

Remarks

This method sets the specified zero-based column value to the given string value. SetString may be used for character or memo fields. No conversions are performed. To set a string field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetString](dotnet_adsdatareader_getstring.md)
