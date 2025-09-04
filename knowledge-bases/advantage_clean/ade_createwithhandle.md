---
title: Ade Createwithhandle
slug: ade_createwithhandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_createwithhandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5891b5b3832dc0bae9400f1bbc14c921a676e07a
---

# Ade Createwithhandle

CreateWithHandle

TAdsConnection.CreateWithHandle

Advantage TDataSet Descendant

| TAdsConnection.CreateWithHandle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Creates a new TAdsConnection component, using an active Advantage Client Engine (ACE) handle.

Syntax

constructor CreateWithHandle(Owner: TComponent; Handle : ADSHANDLE );

Description

Used to construct a new TAdsConnection instance using an active ACE connection handle. After calling CreateWithHandle, a subsequent call to set TAdsConnection.IsActive to True, or a call to the Connect method is not necessary.

If the handle passed in is a database connection, the username and password properties of the TAdsConnection instance will be populated.

This method was designed for use inside trigger functions to create a temporary TAdsConnection instance using an active connection handle that is passed to the trigger.

For applications other than triggers, use the default constructor.

See Also

[CreateFromHandle](ade_createfromhandle.md)
