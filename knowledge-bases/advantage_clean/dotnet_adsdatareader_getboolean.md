---
title: Dotnet Adsdatareader Getboolean
slug: dotnet_adsdatareader_getboolean
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getboolean.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 632cde108909037f528226c63636dd2ea3a83ed1
---

# Dotnet Adsdatareader Getboolean

AdsDataReader.GetBoolean

AdsDataReader.GetBoolean

Advantage .NET Data Provider

| AdsDataReader.GetBoolean  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a Boolean.

public bool GetBoolean( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a Boolean. No conversions are performed, therefore the data retrieved must already be a Boolean or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
