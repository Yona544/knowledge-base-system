---
title: Ade Loginprompt Tadsdictionary
slug: ade_loginprompt__tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_loginprompt__tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 09cc11ddbd045c74c8bd6ef9db07797080cdc483
---

# Ade Loginprompt Tadsdictionary

LoginPrompt

TAdsDictionary.LoginPrompt

Advantage TDataSet Descendant

| TAdsDictionary.LoginPrompt  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Specifies whether a login dialog appears immediately before opening a new database.

Syntax

property LoginPrompt: Boolean;

Description

If LoginPrompt is set to True, a dialog appears to prompt users for a username and password. The current username is read from the TAdsDictionary.Username property, and a standard Login dialog box opens. The dialog prompts for a user name and password combination, and then uses the values entered by the user to attempt a connection.

The OnLogin event is only fired when the LoginPrompt value is True, and can be used to bypass the default login dialog and provide your own dialog or other login method that returns a username and password to be used to establish the connection.

If LoginPrompt is set to False the application must provide a username and password programmatically. Set the [TAdsDictionary.Username](ade_username_tadsdictionary.md) and TAdsDictionary.Password properties prior to setting [TAdsDictionary.IsConnected](ade_isconnected_tadsdictionary.md) to True.

Delphi 6 or greater Users: If using the default login dialog, you must add the DBLogDlg (or QDBLogDlg if using CLX) unit to the uses clause of the unit that declares the connection component. See the Delphi "Controlling Server Login" documentation for more details.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.
