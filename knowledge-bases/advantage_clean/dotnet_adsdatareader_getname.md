---
title: Dotnet Adsdatareader Getname
slug: dotnet_adsdatareader_getname
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getname.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0f6f021c6487b469c82e8eb3d16ca22de908473a
---

# Dotnet Adsdatareader Getname

AdsDataReader.GetName

AdsDataReader.GetName

Advantage .NET Data Provider

| AdsDataReader.GetName  Advantage .NET Data Provider |  |  |  |  |

Gets the name of the specified column.

public String GetName( int columnNumber );

Remarks

Retrieve the name of the column as it is given in the SQL statement or table. If you need the base column name (e.g., for aliased names in SQL statements), you must call [AdsDataReader.GetSchemaTable](dotnet_adsdatareader_getschematable.md), which provides access to that information.

See Also

[GetSchemaTable](dotnet_adsdatareader_getschematable.md)

[GetOrdinal](dotnet_adsdatareader_getordinal.md)
