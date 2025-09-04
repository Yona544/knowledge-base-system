---
title: Dotnet Adscommandbuilder Userowversiononlyinwhereclause
slug: dotnet_adscommandbuilder_userowversiononlyinwhereclause
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_userowversiononlyinwhereclause.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3ef8fa04ef660cdf721964b3767630bcc92e1a2c
---

# Dotnet Adscommandbuilder Userowversiononlyinwhereclause

AdsCommandBuilder.UseRowversionOnlyInWhereClause

AdsCommandBuilder.UseRowversionOnlyInWhereClause

Advantage .NET Data Provider

| AdsCommandBuilder.UseRowversionOnlyInWhereClause  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the flag that controls whether the WHERE clause automatically generated for UPDATE and DELETE statements includes all fields or just the rowversion field.

public bool UseRowversionOnlyInWhereClause {get; set;}

Remarks

By default, this value is False, which means that automatically generated UPDATE and DELETE statements will contain all searchable fields in the WHERE clause. Because rowversion fields are automatically incremented each time a record is updated and guaranteed to be unique within the entire table, using just a rowversion field in the WHERE clause of an UPDATE or DELETE statement is safe. It is also advantageous in that only the rowversion field value will be sent to the server within the query parameters, as opposed to the default behavior which would send all the searchable field data to the server.

See Also

UsePKOnlyInWhereClauseAdsCommandBuilder\_UsePKOnlyInWhereClause
