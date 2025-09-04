---
title: Ade Onlogin Tadsconnection
slug: ade_onlogin_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_onlogin_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a6ac83e72db395717c9c1451dee931b2b65492d9
---

# Ade Onlogin Tadsconnection

OnLogin

TAdsConnection.OnLogin

Advantage TDataSet Descendant

| TAdsConnection.OnLogin  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

OnLogin occurs when an application connects to a database.

Syntax

type TAdsDatabaseLoginEvent = procedure( AdsConnection: TAdsConnection;

var Username : String;

var Password : String ) of object;

 

property OnLogin: TAdsDatabaseLoginEvent;

Description

Write an OnLogin event handler to take specific actions when an application attempts to connect to a database. Values returned in the Username and Password parameters are passed to the Advantage Database Server in the connection attempt.

The OnLogin event is only fired if the [TAdsConnection.LoginPrompt](ade_loginprompt_tadsconnection.md) property is set to True.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[LoginPrompt](ade_loginprompt_tadsconnection.md)

[Username](ade_username_tadsconnection.md)

[Password](ade_password.md)
