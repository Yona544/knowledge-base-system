---
title: Ade Username Tadsconnection
slug: ade_username_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_username_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5e3224a88aaa1e3cc26b82b7f43c330349ff362a
---

# Ade Username Tadsconnection

Username

TAdsConnection.Username

Advantage TDataSet Descendant

| TAdsConnection.Username  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the username to be used in Advantage Data Dictionary connections.

Syntax

property Username: String;

Description

Provide a value in the Username property when establishing connections to an Advantage Data Dictionary.

The Username property is also used to initialize the default login dialog if using [TAdsConnection.LoginPrompt](ade_loginprompt_tadsconnection.md). After a successful Data Dictionary login, the user name used during the login is stored in the Username property.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[Password](ade_password.md)

[LoginPrompt](ade_loginprompt_tadsconnection.md)

[OnLogin](ade_onlogin_tadsconnection.md)
