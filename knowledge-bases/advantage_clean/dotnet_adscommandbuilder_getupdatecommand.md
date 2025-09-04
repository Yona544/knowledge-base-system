---
title: Dotnet Adscommandbuilder Getupdatecommand
slug: dotnet_adscommandbuilder_getupdatecommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_getupdatecommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 6c0be9bfd71cb0f8f0278684153f73efc5cf0cc3
---

# Dotnet Adscommandbuilder Getupdatecommand

AdsCommandBuilder.GetUpdateCommand

AdsCommandBuilder.GetUpdateCommand

Advantage .NET Data Provider

| AdsCommandBuilder.GetUpdateCommand  Advantage .NET Data Provider |  |  |  |  |

Gets the automatically generated AdsCommand object required to perform updates on the database when an application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.md).

public AdsCommand GetUpdateCommand();

Remarks

An application can use the GetUpdateCommand method for informational or troubleshooting purposes because it returns the AdsCommand object to be executed.

You can also use GetUpdateCommand as the basis of a modified command. For example, you might call GetUpdateCommand during development to quickly produce an UPDATE statement and then use that statement directly in your application rather than using the AdsCommandBuilder in the released application.

After the SQL statement is first generated, the application must explicitly call [AdsCommandBuilder.RefreshSchema](dotnet_adscommandbuilder_refreshschema.md) if it changes the statement in any way. Otherwise, the GetUpdateCommand will be still be using information from the previous statement, which might not be correct. The SQL statements are first generated either when the application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.md) or GetUpdateCommand.
