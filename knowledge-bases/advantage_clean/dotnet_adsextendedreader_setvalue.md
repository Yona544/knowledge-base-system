---
title: Dotnet Adsextendedreader Setvalue
slug: dotnet_adsextendedreader_setvalue
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setvalue.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5760ad2d0a1ff1319cac83948c8393ab4a197df6
---

# Dotnet Adsextendedreader Setvalue

AdsExtendedReader.SetValue

AdsExtendedReader.SetValue

Advantage .NET Data Provider

| AdsExtendedReader.SetValue  Advantage .NET Data Provider |  |  |  |  |

Sets the value of the specified column in its native format.

public void SetValue( int iCol, Object value );

Remarks

This method sets the specified zero-based column value to the given Object value. SetValue will attempt to set the value for the field based on the type of the value object. No conversions are performed. Calling SetValue with an incorrect type will cause an exception. For example, setting an integer value with the string "1" will not succeed. Calling SetValue with an object of type DBNull or Empty will set the field value to null.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)
