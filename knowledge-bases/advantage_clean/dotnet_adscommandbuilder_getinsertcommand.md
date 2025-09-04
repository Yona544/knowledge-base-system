---
title: Dotnet Adscommandbuilder Getinsertcommand
slug: dotnet_adscommandbuilder_getinsertcommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_getinsertcommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 166ef651dc6c0dfcee906e7003460ce39daad475
---

# Dotnet Adscommandbuilder Getinsertcommand

AdsCommandBuilder.GetInsertCommand

AdsCommandBuilder.GetInsertCommand

Advantage .NET Data Provider

| AdsCommandBuilder.GetInsertCommand  Advantage .NET Data Provider |  |  |  |  |

Gets the automatically generated AdsCommand object required to perform inserts on the database when an application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.md).

public AdsCommand GetInsertCommand();

Remarks

An application can use the GetInsertCommand method for informational or troubleshooting purposes because it returns the AdsCommand object to be executed.

You can also use GetInsertCommand as the basis of a modified command. For example, you might call GetInsertCommand during development to quickly produce an INSERT statement and then use that statement directly in your application rather than using the AdsCommandBuilder in the released application.

After the SQL statement is first generated, the application must explicitly call [AdsCommandBuilder.RefreshSchema](dotnet_adscommandbuilder_refreshschema.md) if it changes the statement in any way. Otherwise, the GetInsertCommand will be still be using information from the previous statement, which might not be correct. The SQL statements are first generated either when the application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.md) or [GetInsertCommand](dotnet_adscommandbuilder_getinsertcommand.md).
