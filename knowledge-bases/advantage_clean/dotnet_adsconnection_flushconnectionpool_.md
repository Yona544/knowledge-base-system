---
title: Dotnet Adsconnection Flushconnectionpool
slug: dotnet_adsconnection_flushconnectionpool_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_flushconnectionpool_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 497ad4ed434f952722f33806ec786e865d673d6b
---

# Dotnet Adsconnection Flushconnectionpool

AdsConnection.FlushConnectionPool()

AdsConnection.FlushConnectionPool()

Advantage .NET Data Provider

| AdsConnection.FlushConnectionPool()  Advantage .NET Data Provider |  |  |  |  |

Closes all unused connections in all connection pools.

public void FlushConnectionPool();

Remarks

This method will close all unused connections in all connection pools. Note that the connection pool is application-wide, so this will close all unused connections in the application.

See Also

[AdsConnection.FlushConnectionPool( string )](dotnet_adsconnection_flushconnectionpool_string_.md)
