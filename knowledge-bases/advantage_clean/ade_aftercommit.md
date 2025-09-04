---
title: Ade Aftercommit
slug: ade_aftercommit
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_aftercommit.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 09bd384f480c22789745cf21a3eb2ca9c3fa1195
---

# Ade Aftercommit

AfterCommit

TAdsConnection.AfterCommit

Advantage TDataSet Descendant

| TAdsConnection.AfterCommit  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

AfterCommit occurs after an application completes a request to commit modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property AfterCommit: TNotifyEvent;

Description

Write an AfterCommit event handler to take specific action after an application commits changes to the current transaction.
