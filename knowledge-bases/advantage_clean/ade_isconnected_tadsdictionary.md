---
title: Ade Isconnected Tadsdictionary
slug: ade_isconnected_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_isconnected_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e12de283cb6ff30b11531a5932efd4b76eb74732
---

# Ade Isconnected Tadsdictionary

IsConnected

TAdsDictionary.IsConnected

Advantage TDataSet Descendant

| TAdsDictionary.IsConnected  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Specifies whether or not the connection has been established.

Syntax

property IsConnected: Boolean;

Description

Use IsConnected to determine or set a connection. If the setting IsConnected to True:

- Triggers the OnConnect event handler if one is defined for the data dictionary component.

- Opens a connection to the server.

If an error occurs during the getting of the connection, IsConnected is set to False.
