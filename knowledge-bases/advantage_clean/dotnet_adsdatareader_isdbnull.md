---
title: Dotnet Adsdatareader Isdbnull
slug: dotnet_adsdatareader_isdbnull
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_isdbnull.htm
source: Advantage CHM
tags:
  - dotnet
checksum: eb31223d46c62b9db9cdea2d4ad9eb1cff5cc353
---

# Dotnet Adsdatareader Isdbnull

AdsDataReader.IsDBNull

AdsDataReader.IsDBNull

Advantage .NET Data Provider

| AdsDataReader.IsDBNull  Advantage .NET Data Provider |  |  |  |  |

Indicates whether or not the column contains a null.

public bool IsDBNull( int columnNumber );

Remarks

This returns True if the specified zero-based column has a null value. Call this method to check for null column values before calling the typed get methods (for example, [GetBoolean](dotnet_adsdatareader_getboolean.md), [GetString](dotnet_adsdatareader_getstring.md), etc.) to avoid raising an error.

DBF tables (TableType of CDX or NTX) do not have null values except for date fields, so this will always return False for non-date fields unless the connection string property DbfsUseNulls is set to True. See [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md).

See Also

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)
