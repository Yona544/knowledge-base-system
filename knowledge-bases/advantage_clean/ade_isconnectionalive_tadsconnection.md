---
title: Ade Isconnectionalive Tadsconnection
slug: ade_isconnectionalive_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_isconnectionalive_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d3db40abce4788368d5bb67e8e66be29738d35db
---

# Ade Isconnectionalive Tadsconnection

IsConnectionAlive

IsConnectionAlive

Advantage TDataSet Descendant

| IsConnectionAlive  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Indicates whether the underlying connection to Advantage Database Server is still active.

Syntax

property IsConnectionAlive: Boolean;

Description

IsConnectionAlive is a read-only property that can be used by an application to test if the connection to Advantage Database Server is still usable. If this property returns false, it indicates that the connection has been lost. Reasons for a lost connection include network failure, server failure, Advantage Database Server failure, or cluster node failover. If an application needs to stay connected at all times, it can use this property to test a connection. If the connection is lost, a possible course of action is to close all objects (tables, cursors, SQL statements, and the connection itself) and attempt to reconnect to the server, which may succeed if the server was stopped momentarily or if it is part of a cluster and was moved to another node by the cluster manager.

Note This property will return false if the TAdsConnection.IsConnected property has not been set to true.

See Also

[IsConnected](ade_isconnected_tadsconnection.md)
