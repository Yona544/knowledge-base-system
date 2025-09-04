---
title: Ade Onlogin Tadsdictionary
slug: ade_onlogin_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_onlogin_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2ab1e0092ef5bac9c5758f4e302960c6bcb3ac92
---

# Ade Onlogin Tadsdictionary

OnLogin

TAdsDictionary.OnLogin

Advantage TDataSet Descendant

| TAdsDictionary.OnLogin  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

OnLogin occurs when an application connects to a database.

Syntax

type TAdsDatabaseLoginEvent = procedure( AdsConnection: TAdsConnection;

var Username : String;

var Password : String ) of object;

 

property OnLogin: TAdsDatabaseLoginEvent;

Description

Write an OnLogin event handler to take specific actions when an application attempts to connect to a database. Values returned in the Username and Password parameters are passed to the Advantage Database Server in the connection attempt.

The OnLogin event is only fired if the [TAdsDictionary.LoginPrompt](ade_loginprompt__tadsdictionary.md) property is set to True.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.
