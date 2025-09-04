---
title: Dotnet Adsconnection Servername
slug: dotnet_adsconnection_servername
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_servername.htm
source: Advantage CHM
tags:
  - dotnet
checksum: b5d70284897c324a138d987b47e588b5cb2522cc
---

# Dotnet Adsconnection Servername

AdsConnection.ServerName

AdsConnection.ServerName

Advantage .NET Data Provider

| AdsConnection.ServerName  Advantage .NET Data Provider |  |  |  |  |

Gets the server name.

public string ServerName {get;}

Remarks

Retrieves the server name associated with a connection. ServerName returns the name of the server on which the connected Advantage server is loaded. The server name will not include any volume or share information. If accessing data on a local drive and using Advantage Local Server, the drive letter is returned.
