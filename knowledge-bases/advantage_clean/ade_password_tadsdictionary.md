---
title: Ade Password Tadsdictionary
slug: ade_password_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_password_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: bfb0749c3a363f3ef3a167244c8026ff5a26031a
---

# Ade Password Tadsdictionary

Password

TAdsDictionary.Password

Advantage TDataSet Descendant

| TAdsDictionary.Password  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Specifies the password to be used in Advantage Data Dictionary connections.

Syntax

property Password: String;

Description

Provide a value in the Password property when establishing connections to an Advantage Data Dictionary.

Setting the Password property directly is not recommended. As an alternative, use a login dialog and/or the TAdsDictionary.OnLogin event to control server logins.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.
