---
title: Dotnet Adscommandbuilder Quotesuffix
slug: dotnet_adscommandbuilder_quotesuffix
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_quotesuffix.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 7271dc5ff49281f1e6a41ef976104500c1768c32
---

# Dotnet Adscommandbuilder Quotesuffix

AdsCommandBuilder.QuoteSuffix

AdsCommandBuilder.QuoteSuffix

Advantage .NET Data Provider

| AdsCommandBuilder.QuoteSuffix  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the ending character to use when for delimiting Advantage object names (e.g., tables and columns).

public string QuoteSuffix {get; set;}

Remarks

Advantage table names and column names can contain special characters such as spaces. If so, they must be delimited by either double quotes or by square brackets in order to be recognized correctly by the SQL parser. By default the QuoteSuffix property is a right square bracket (]). It should not be necessary to set this property.

See Also

[QuotePrefix](dotnet_adscommandbuilder_quoteprefix.md)
