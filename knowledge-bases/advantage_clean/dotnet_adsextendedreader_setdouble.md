---
title: Dotnet Adsextendedreader Setdouble
slug: dotnet_adsextendedreader_setdouble
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setdouble.htm
source: Advantage CHM
tags:
  - dotnet
checksum: a0c4cfe513efc1fa61cac9a35f581040d948e00f
---

# Dotnet Adsextendedreader Setdouble

AdsExtendedReader.SetDouble

AdsExtendedReader.SetDouble

Advantage .NET Data Provider

| AdsExtendedReader.SetDouble  Advantage .NET Data Provider |  |  |  |  |

Stores the given double value in the specified column.

public void SetDouble( int iCol, double value );

Remarks

This method sets the specified zero-based column value to the given double value. No conversions are performed. To set a double field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetDouble](dotnet_adsdatareader_getdouble.md)
