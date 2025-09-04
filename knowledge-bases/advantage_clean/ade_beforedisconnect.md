---
title: Ade Beforedisconnect
slug: ade_beforedisconnect
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_beforedisconnect.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: edf85983ecb811bd17e85d09733eac45818aa4b0
---

# Ade Beforedisconnect

BeforeDisconnect

TAdsConnection.BeforeDisconnect

Advantage TDataSet Descendant

| TAdsConnection.BeforeDisconnect  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

BeforeDisconnect occurs immediately before closing a connection.

Syntax

property BeforeDisconnect: TNotifyEvent;

Description

Write a BeforeDisconnect event handler to take application-specific actions before the connection component closes a connection to the Advantage Database Server.

See Also

[AfterDisconnect](ade_afterdisconnect.md)
