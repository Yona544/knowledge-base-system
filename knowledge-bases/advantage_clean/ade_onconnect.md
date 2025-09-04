---
title: Ade Onconnect
slug: ade_onconnect
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_onconnect.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6501e650e992652011d42c6233f4f1b7d9fd4558
---

# Ade Onconnect

OnConnect

TAdsConnection.OnConnect

Advantage TDataSet Descendant

| TAdsConnection.OnConnect  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

OnConnect occurs when an application makes a request to get a connection.

Syntax

type TNotifyEvent = procedure of object;

 

property OnConnect: TNotifyEvent;

Description

Write an OnConnect event handler to take specific action when an application makes a request to get a connection.
