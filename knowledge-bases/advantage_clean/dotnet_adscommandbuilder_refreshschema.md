---
title: Dotnet Adscommandbuilder Refreshschema
slug: dotnet_adscommandbuilder_refreshschema
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_refreshschema.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ab6ae7398c2fc386f7fd22ba8fdc0624c1febcfd
---

# Dotnet Adscommandbuilder Refreshschema

AdsCommandBuilder.RefreshSchema

AdsCommandBuilder.RefreshSchema

Advantage .NET Data Provider

| AdsCommandBuilder.RefreshSchema  Advantage .NET Data Provider |  |  |  |  |

Refreshes the database schema information used to generate INSERT, UPDATE, or DELETE statements.

public void RefreshSchema();

Remarks

An application should call RefreshSchema whenever the SelectCommand value of the [AdsDataAdapter](dotnet_adsdataadapter.md) associated with the AdsCommandBuilder changes. The SelectCommand is not associated directly with the AdsCommandBuilder, so it has no way of automatically detecting when it is changed.
