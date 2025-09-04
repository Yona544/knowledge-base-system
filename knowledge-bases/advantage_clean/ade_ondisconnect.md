---
title: Ade Ondisconnect
slug: ade_ondisconnect
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ondisconnect.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6ff669fc45d9b55cb21a0a8db74a1a3092d335d5
---

# Ade Ondisconnect

OnDisconnect

TAdsConnection.OnDisconnect

Advantage TDataSet Descendant

| TAdsConnection.OnDisconnect  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

OnDisconnect occurs when an application makes a request to release a connection.

Syntax

type TNotifyEvent = procedure of object;

 

property OnDisconnect: TNotifyEvent;

Description

Write an OnDisconnect event handler to take specific action when an application makes a request to release a connection.
