---
title: Ade Sethandle
slug: ade_sethandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sethandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a9860f56bc57098e68bca2af9aa854c20eb5bfb0
---

# Ade Sethandle

SetHandle

TAdsConnection.SetHandle

Advantage TDataSet Descendant

| TAdsConnection.SetHandle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Sets the connection handle of a TAdsConnection object to an already working ADS connection handle.

Syntax

procedure SetHandle( hConnection : ADSHANDLE );

Parameters

| hConnection (I) | An already working connection handle provided to a trigger or created by an ACE API connect call. |

Description

SetHandle can be used to place an active ACE connection handle into an existing TAdsConnection instance. After calling SetHandle, a subsequent call to set TAdsConnection.IsActive to True, or a call to the Connect method is not necessary.

If the handle passed in is a database connection, the username and password properties of the TAdsConnection instance will be populated.

This method was designed for use inside extended procedures to create a temporary TAdsConnection instance using an active connection handle that is passed to the procedure. Any other use of this method is discouraged.

Note TAdsConnection will not disconnect a connection supplied by SetHandle() when destroyed or if SetConnected is assigned False. In other words, the connection given to SetHandle() was not created by TAdsConnection and therefore will not be destroyed (disconnected) by TAdsConnection. See [Triggers](master_triggers.md) for more information.
