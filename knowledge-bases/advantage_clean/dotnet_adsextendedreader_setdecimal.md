---
title: Dotnet Adsextendedreader Setdecimal
slug: dotnet_adsextendedreader_setdecimal
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setdecimal.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c2381ec6e5b2df416c0cbb2d52e5dbacf185c93b
---

# Dotnet Adsextendedreader Setdecimal

AdsExtendedReader.SetDecimal

AdsExtendedReader.SetDecimal

Advantage .NET Data Provider

| AdsExtendedReader.SetDecimal  Advantage .NET Data Provider |  |  |  |  |

Stores the given Decimal value in the specified column.

public void SetDecimal( int iCol, Decimal value );

Remarks

This method sets the specified zero-based column value to the given Decimal value. SetDecimal can be used to store money type field values. No conversions are performed. To set a money field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetDecimal](dotnet_adsdatareader_getdecimal.md)
