---
title: Ade Connectiontype
slug: ade_connectiontype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_connectiontype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 507609b9cd7f33bee6d31b4bdee162b14b8ecfb5
---

# Ade Connectiontype

ConnectionType

TAdsConnection.ConnectionType

Advantage TDataSet Descendant

| TAdsConnection.ConnectionType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the type of connection to the server.

Syntax

property ConnectionType: String;

Description

If there is a connection, this property will return that either the AIS (Advantage Internet Server), LOCAL (Advantage Local Server), or REMOTE (Advantage Database Server) is being used. The string returned is not guaranteed to be all upper case, so a case insensitive comparison should be done if you want to do comparison to the return value.If there is no connection, the return string is empty.
