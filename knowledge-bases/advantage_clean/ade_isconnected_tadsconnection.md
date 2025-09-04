---
title: Ade Isconnected Tadsconnection
slug: ade_isconnected_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_isconnected_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 15cd818e73044c41d9e5c01c1b298ad25015d2ed
---

# Ade Isconnected Tadsconnection

IsConnected

TAdsConnection.IsConnected

Advantage TDataSet Descendant

| TAdsConnection.IsConnected  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies whether or not the connection has been established.

Syntax

property IsConnected: Boolean;

Description

Use IsConnected to determine or set a connection.

Setting IsConnected to True:

- Triggers the OnConnect event handler if one is defined for the connection component.

- Opens a connection to the server.

If an error occurs during the getting of the connection, IsConnected is set to False.

Note Setting the Active property of a TAdsTable attached to a TAdsConnection component to True will cause the TAdsConnection component to request a connection.

See also

[IsConnectionAlive](ade_isconnectionalive_tadsconnection.md)
