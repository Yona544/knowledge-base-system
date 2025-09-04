---
title: Dotnet Adsconnection Isdictionaryconn
slug: dotnet_adsconnection_isdictionaryconn
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_isdictionaryconn.htm
source: Advantage CHM
tags:
  - dotnet
checksum: bdb341ba1f6d6b63c3b118651f24d3745367fbf2
---

# Dotnet Adsconnection Isdictionaryconn

AdsConnection.IsDictionaryConn

AdsConnection.IsDictionaryConn

Advantage .NET Data Provider

| AdsConnection.IsDictionaryConn  Advantage .NET Data Provider |  |  |  |  |

Returns whether an open connection is an Advantage Data Dictionary connection.

public bool IsDictionaryConn{ get; }

Remarks

IsDictionaryConn checks an open connection and returns true if the connection is a data dictionary connection (connection types ADS\_DATABASE\_CONNECTION or ADS\_SYS\_ADMIN\_CONNECTION). Otherwise false is returned.

Note If the connection is not open, calling IsDictionaryConn will cause an exception.
