---
title: Ade Servername
slug: ade_servername
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_servername.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d22612c0a7e451f9db5722608861368d3ee69f44
---

# Ade Servername

ServerName

TAdsConnection.ServerName

Advantage TDataSet Descendant

| TAdsConnection.ServerName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Read-only property that will retrieve the server name that the connection is on.

Syntax

property ServerName: String;

Description

This is the property to retrieve if there is a question as to the name of the server to which TAdsConnection is connected. The connection must be established before getting this property. If accessing data on a local drive and using [Advantage Local Server](master_advantage_local_server.md), the drive letter is returned.
