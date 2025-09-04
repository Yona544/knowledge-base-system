---
title: Dotnet Adsconnection Database
slug: dotnet_adsconnection_database
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_database.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 04fc34622deba7da46264a60f83b0b29b1ec7608
---

# Dotnet Adsconnection Database

AdsConnection.Database

AdsConnection.Database

Advantage .NET Data Provider

| AdsConnection.Database  Advantage .NET Data Provider |  |  |  |  |

Gets the name of the database that the connection object represents.

public string Database {get;}

Remarks

Gets the name of the database that the connection object represents. If the Initial Catalog property was provided in the [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md), it will be returned. Otherwise, it will return the full connect path. An empty string is returned if no connection path information is available.
