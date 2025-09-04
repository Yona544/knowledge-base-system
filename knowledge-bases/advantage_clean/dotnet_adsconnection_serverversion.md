---
title: Dotnet Adsconnection Serverversion
slug: dotnet_adsconnection_serverversion
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_serverversion.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2965750bf2d3c4b6332050d3d6600e4736ed0de4
---

# Dotnet Adsconnection Serverversion

AdsConnection.ServerVersion

AdsConnection.ServerVersion

Advantage .NET Data Provider

| AdsConnection.ServerVersion  Advantage .NET Data Provider |  |  |  |  |

Retrieves the version of the Advantage Database Server to which the object is connected.

public string ServerVersion {get;}

Remarks

This property retrieves a string that represents the version of the Advantage server to which the connection is made. The connection must be open in order to retrieve the property. The first time the property is retrieved, it results in a call to the server.
