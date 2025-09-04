---
title: Master Accessing An Advantage Data Dictionary With The Advantage Tdataset Descendant
slug: master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm
source: Advantage CHM
tags:
  - master
checksum: d26875496ec223b41adee9daf67cba712c85116d
---

# Master Accessing An Advantage Data Dictionary With The Advantage Tdataset Descendant

Accessing an Advantage Data Dictionary with the Advantage TDataSet Descendant

Accessing an Advantage Data Dictionary with the Advantage TDataSet Descendant

Advantage Concepts

| Accessing an Advantage Data Dictionary with the Advantage TDataSet Descendant  Advantage Concepts |  |  |  |  |

Access to an Advantage Data Dictionary through the Advantage TDataSet Descendant solution is accomplished through the use of the TAdsConnection component. Advantage Data Dictionary access is not supported with stand-alone TAdsTable/TAdsQuery components. TAdsTable and TAdsQuery components that access tables in an Advantage Data Dictionary must be attached to a TAdsConnection component.

A TAdsConnection component is considered a "Dictionary Connection" if the AliasName property is set to a dictionary alias, or if the ConnectPath property ends with ".add" (for example, x:\mydatafiles\mydictionary.add). The TAdsConnection.IsDictionaryConn property can be used after a connection has been made do determine if the connection is a standard Advantage connection or a connection to an Advantage Data Dictionary.

Several properties and the OnLogin event exist in the TAdsConnection component to facilitate Advantage Data Dictionary access:

Properties

IsDictionaryConn

LoginPrompt

Password

Username

Events

OnLogin

Database login can be controlled through the use of the LoginPrompt, Username, and Password properties in conjunction with the OnLogin event.

Once a table has been configured to use a TAdsConnection component (preferably through the DatabaseName property, as opposed to the AdsConnection property) all tables and views available in the Advantage Data Dictionary can be displayed in the TableName property drop-down list.

Advantage Data Dictionary creation and administration is accomplished through the use of the Advantage Database Manager utility included in the Advantage Data Architect application.

Administrative tasks can also be embedded directly into your application through the use of the TAdsDictionary component.

See the Advantage TDataSet Descendant Help documentation (ADE.HLP) for more information. (Note that each of the Advantage products and their corresponding Help files are installed separately.)
