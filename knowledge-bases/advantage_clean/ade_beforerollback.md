---
title: Ade Beforerollback
slug: ade_beforerollback
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_beforerollback.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2b4f6b5b085aa645bef79283b5e1e61944b805e3
---

# Ade Beforerollback

BeforeRollback

TAdsConnection.BeforeRollback

Advantage TDataSet Descendant

| TAdsConnection.BeforeRollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

BeforeRollback occurs before an application makes a request to rollback modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property BeforeRollback: TNotifyEvent;

Description

Write a BeforeRollback event handler to take specific action before an application rolls back changes to the current transaction.
