---
title: Dotnet Adsconnection State
slug: dotnet_adsconnection_state
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_state.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ea591df83f281b29b8dac4f504ba629ebe87e8be
---

# Dotnet Adsconnection State

AdsConnection.State

AdsConnection.State

Advantage .NET Data Provider

| AdsConnection.State  Advantage .NET Data Provider |  |  |  |  |

Gets the current state of the connection.

public ConnectionState State {get;}

Remarks

Gets the current state of the connection. It returns either ConnectionState.Open (if the connection to Advantage Database Server or Advantage Local Server is active) or ConnectionState.Closed if there is no active connection.

This property is defined to return a bitwise combination ConnectionState enumeration values. Currently, the Advantage .NET Data Provider uses only the Open and Closed values; the remaining values are reserved for future use by Microsoft. For best compatibility with future versions, you should check the values as a bitmask.

Example

if (( conn.State & ConnectionState.Open ) == 0 )

// It is not open

conn.Open();

See Also

[AdsConnection.Open](dotnet_adsconnection_open.md)

[AdsConnection.Close](dotnet_adsconnection_close.md)
