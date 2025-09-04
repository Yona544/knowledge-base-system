---
title: Dotnet Adsconnectionstringbuilder Connectionstring
slug: dotnet_adsconnectionstringbuilder_connectionstring
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnectionstringbuilder_connectionstring.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 45ad6c7bcb25130baccf635381843d6229b6c157
---

# Dotnet Adsconnectionstringbuilder Connectionstring

AdsConnectionStringBuilder.ConnectionString

AdsConnectionStringBuilder.ConnectionString

Advantage .NET Data Provider

| AdsConnectionStringBuilder.ConnectionString  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the connection string.

public string ConnectionString {get; set;}

Remarks

This property can be used to set or retrieve the full connection string. If the individual properties are set, then the full connection string can be retrieved with this property and assigned to an AdsConnection object.

Example

AdsConnectionStringBuilder builder =

new AdsConnectionStringBuilder();

 

builder.DataSource = @"c:\data";

builder.ServerType = "local";

 

AdsConnection conn = new AdsConnection();

conn.ConnectionString = builder.ConnectionString;

conn.Open();

See Also

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)
