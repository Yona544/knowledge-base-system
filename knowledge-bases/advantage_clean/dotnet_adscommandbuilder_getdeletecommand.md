---
title: Dotnet Adscommandbuilder Getdeletecommand
slug: dotnet_adscommandbuilder_getdeletecommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_getdeletecommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: bc1fc897a6b3f9d240f12c617183ea35fb00a40a
---

# Dotnet Adscommandbuilder Getdeletecommand

AdsCommandBuilder.GetDeleteCommand

AdsCommandBuilder.GetDeleteCommand

Advantage .NET Data Provider

| AdsCommandBuilder.GetDeleteCommand  Advantage .NET Data Provider |  |  |  |  |

Gets the automatically generated AdsCommand object required to perform deletions on the database when an application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.md).

public AdsCommand GetDeleteCommand();

Remarks

An application can use the GetDeleteCommand method for informational or troubleshooting purposes because it returns the AdsCommand object to be executed.

You can also use GetDeleteCommand as the basis of a modified command. For example, you might call GetDeleteCommand during development to quickly produce a DELETE statement and then use that statement directly in your application rather than using the AdsCommandBuilder in the released application.

After the SQL statement is first generated, the application must explicitly call [AdsCommandBuilder.RefreshSchema](dotnet_adscommandbuilder_refreshschema.md) if it changes the statement in any way. Otherwise, the GetDeleteCommand will be still be using information from the previous statement, which might not be correct. The SQL statements are first generated either when the application calls Update or GetDeleteCommand.
