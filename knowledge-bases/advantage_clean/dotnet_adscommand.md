---
title: Dotnet Adscommand
slug: dotnet_adscommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 24d9fd28acc829ad4c9554c57630bd463172f1de
---

# Dotnet Adscommand

AdsCommand

AdsCommand

Advantage .NET Data Provider

| AdsCommand  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsCommand

Implements: System.Data.IDbCommand

[Constructors](dotnet_adscommand_constructors.md)

[Properties](dotnet_adscommand_properties.md)

[Methods](dotnet_adscommand_methods.md)

[Events](dotnet_adscommand_progressmessage.md)

An AdsCommand object represents an SQL statement or stored procedure to execute or a table to directly open on Advantage Database Server or Advantage Local Server.

To use an AdsCommand object, the application must associate the command with the AdsConnection object. This can be done in one of three ways. If you use the [AdsConnection.CreateCommand()](dotnet_adsconnection_createcommand.md) method to create a new command object, the command object will be associated with the connection from which it was created automatically. Alternatively, you can use one of the AdsCommand constructors that accepts an AdsConnection object. Or lastly, you can assign the AdsConnection object to the [AdsCommand.Connection](dotnet_adscommand_connection.md) property after the command object has been created.
