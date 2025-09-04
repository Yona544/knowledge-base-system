---
title: Dotnet Adsdatareader Getdecimal
slug: dotnet_adsdatareader_getdecimal
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getdecimal.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ee30c505d01c3ace3e3bce0495a84b36d564365c
---

# Dotnet Adsdatareader Getdecimal

AdsDataReader.GetDecimal

AdsDataReader.GetDecimal

Advantage .NET Data Provider

| AdsDataReader.GetDecimal  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a Decimal object.

public Decimal GetDecimal( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a Decimal object. No conversions are performed, therefore the data retrieved must already be a Decimal or an exception is generated. It can be used to retrieve numeric, money, and integer field values. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
