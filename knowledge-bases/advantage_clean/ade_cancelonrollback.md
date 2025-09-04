---
title: Ade Cancelonrollback
slug: ade_cancelonrollback
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_cancelonrollback.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 607ec6c9ab8db0394fb6adf287302dc0b0d39e8d
---

# Ade Cancelonrollback

CancelOnRollback

TAdsConnection.CancelOnRollback

Advantage TDataSet Descendant

| TAdsConnection.CancelOnRollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Controls dataset behavior when a [Rollback](ade_rollback.md) operation is performed.

Syntax

property CancelOnRollback : boolean;

Description

CancelOnRollback is TRUE by default. This property controls the behavior of the Rollback method. If TRUE, when a Rollback is performed all datasets attached to the connection will cancel any pending updates and return to a browse state. If FALSE, the transaction will be rolled back, but datasets attached to the connection will remain in the state they were in before the rollback operation.

See Also

[BeginTransaction](ade_begintransaction.md)

[Rollback](ade_rollback.md)
