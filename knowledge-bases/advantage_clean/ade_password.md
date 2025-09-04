---
title: Ade Password
slug: ade_password
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_password.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b507680008ffd013b0b0b88c5e0b80cb66c55ea3
---

# Ade Password

Password

TAdsConnection.Password

Advantage TDataSet Descendant

| TAdsConnection.Password  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the password to be used in Advantage Data Dictionary connections.

Syntax

property Password: String;

Description

Provide a value in the Password property when establishing connections to an Advantage Data Dictionary.

Setting the Password property directly is not recommended. As an alternative, use a login dialog and/or the [TAdsConnection.OnLogin](ade_onlogin_tadsconnection.md) event to control server logins.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[Username](ade_username_tadsconnection.md)

[LoginPrompt](ade_loginprompt_tadsconnection.md)

[OnLogin](ade_onlogin_tadsconnection.md)
