---
title: Ade Username Tadsdictionary
slug: ade_username_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_username_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fc2be81dc253b6ab4e74d51e1719ec0710f163af
---

# Ade Username Tadsdictionary

Username

TAdsDictionary.Username

Advantage TDataSet Descendant

| TAdsDictionary.Username  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Specifies the username to be used in Advantage Data Dictionary connections.

Syntax

property Username: String;

Description

Provide a value in the Username property when establishing connections to an Advantage Data Dictionary.

The Username property is also used to initialize the default login dialog if using [TAdsDictionary.LoginPrompt](ade_loginprompt__tadsdictionary.md). After a successful Data Dictionary login, the user name used during the login is stored in the Username property.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.
