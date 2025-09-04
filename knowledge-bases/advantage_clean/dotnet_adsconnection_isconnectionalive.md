---
title: Dotnet Adsconnection Isconnectionalive
slug: dotnet_adsconnection_isconnectionalive
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_isconnectionalive.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 258c38f759a6591f983c14095802ca2aff0932b7
---

# Dotnet Adsconnection Isconnectionalive

AdsConnection.IsConnectionAlive

AdsConnection.IsConnectionAlive

Advantage .NET Data Provider

| AdsConnection.IsConnectionAlive  Advantage .NET Data Provider |  |  |  |  |

Indicates whether the underlying connection to Advantage Database Server is still active.

public bool IsConnectionAlive{ get; }

Remarks

IsConnectionAlive is a read-only property that can be used by an application to test if the connection to Advantage Database Server is still usable. If this property returns false, it indicates that the connection has been lost. Reasons for a lost connection include network failure, server failure, Advantage Database Server failure, or cluster node failover. If an application needs to stay connected at all times, it can use this property to test a connection. If the connection is lost, a possible course of action is to close all objects (tables, cursors, SQL statements, and the connection itself) and attempt to reconnect to the server, which may succeed if the server was stopped momentarily or if it is part of a cluster and was moved to another node by the cluster manager.

If an application creates and deletes connections as needed, then it is unlikely that it will need to use this property. With the .NET data provider, this type of connection usage is very efficient because connection pooling is turned on by default, and the connection pool manager automatically verifies that a connection is active before returning it to the caller.

Note If this property is tested before a connection has been opened (AdsConnection.Open) or after it has been closed (AdsConnection.Close), it will throw an InvalidOperationException exception.
