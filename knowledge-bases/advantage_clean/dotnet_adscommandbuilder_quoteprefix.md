---
title: Dotnet Adscommandbuilder Quoteprefix
slug: dotnet_adscommandbuilder_quoteprefix
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_quoteprefix.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 6267584d09c56c3eb136193ea3b84dd10708ff6d
---

# Dotnet Adscommandbuilder Quoteprefix

AdsCommandBuilder.QuotePrefix

AdsCommandBuilder.QuotePrefix

Advantage .NET Data Provider

| AdsCommandBuilder.QuotePrefix  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the beginning character to use when for delimiting Advantage object names (e.g., tables and columns).

public string QuotePrefix {get; set;}

Remarks

Advantage table names and column names can contain special characters such as spaces. If so, they must be delimited by either double quotes or by square brackets in order to be recognized correctly by the SQL parser. By default the QuotePrefix property is a left square bracket ([). It should not be necessary to set this property.

See Also

[AdsCommandBuilder.QuoteSuffix](dotnet_adscommandbuilder_quotesuffix.md)
