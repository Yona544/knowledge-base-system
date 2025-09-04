---
title: Dotnet Adsconnection Connectionhandle
slug: dotnet_adsconnection_connectionhandle
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_connectionhandle.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 25122709caf1289109b4def0fce88ca65d31776b
---

# Dotnet Adsconnection Connectionhandle

AdsConnection.ConnectionHandle

AdsConnection.ConnectionHandle

Advantage .NET Data Provider

| AdsConnection.ConnectionHandle  Advantage .NET Data Provider |  |  |  |  |

Returns the internal handle used by the Advantage Client Engine.

public IntPtr ConnectionHandle {get;}

Remarks

This handle is currently only used internally by the Advantage Data Provider. It is publicly accessible for possible future enhancements.

Note The AdsConnection must be open when getting the ConnectionHandle.
