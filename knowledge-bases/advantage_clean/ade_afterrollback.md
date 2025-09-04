---
title: Ade Afterrollback
slug: ade_afterrollback
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_afterrollback.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 23060f5fb75cd1d2c565b0a59b5efd09ce78e822
---

# Ade Afterrollback

AfterRollback

TAdsConnection.AfterRollback

Advantage TDataSet Descendant

| TAdsConnection.AfterRollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

AfterRollback occurs after an application completes a request to rollback modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property AfterRollback: TNotifyEvent;

Description

Write an AfterRollback event handler to take specific action after an application rolls back changes to the current transaction.
