---
title: Ade Isdictionaryconn
slug: ade_isdictionaryconn
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_isdictionaryconn.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d603ab228ef6ee85891633970edf8103c99b2d2a
---

# Ade Isdictionaryconn

IsDictionaryConn

TAdsConnection.IsDictionaryConn

Advantage TDataSet Descendant

| TAdsConnection.IsDictionaryConn  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies if the connection is to an Advantage Data Dictionary.

Syntax

property IsDictionaryConn: Boolean;

Description

IsDictionaryConn can be retrieved after the IsConnected property is set to TRUE to determine whether the connection is an Advantage Data Dictionary connection, or a standard Advantage connection.

Note You are not required to check if a connection is to an Advantage Data Dictionary, this property is only provided as an information property you may find useful when updating existing applications that may want to change their behavior depending on the connection type. If you specify a dictionary alias or connection path (for example, x:\mydata\mydictionary.add) and that file can not be opened an error will be returned, you do NOT have to inspect IsDictionaryConn to determine if the application opened the dictionary.
