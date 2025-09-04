---
title: Ade Createfromhandle
slug: ade_createfromhandle
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_createfromhandle.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e25c4696f808c7ca43e4bc922b4d0f505a2cda32
---

# Ade Createfromhandle

CreateFromHandle

TAdsConnection.CreateFromHandle

Advantage TDataSet Descendant

| TAdsConnection.CreateFromHandle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Creates a new TAdsConnection component, using an active Advantage Client Engine (ACE) handle.

Syntax

constructor CreateFromHandle(Owner: TComponent; Handle : ADSHANDLE; strName : string );

Description

Used to setup an active TAdsConnection instance from an existing ACE handle, but unlike [CreateWithHandle](ade_createwithhandle.md) which takes on the ACE connection handle, this method will get its own new ACE connection, which will be based on the values it takes from the existing connection.

If the handle passed in is a database connection, the username and password properties of the TAdsConnection instance will be populated.

 

See Also

[CreateWithHandle](ade_createwithhandle.md)
