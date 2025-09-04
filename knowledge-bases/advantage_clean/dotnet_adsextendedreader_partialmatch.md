---
title: Dotnet Adsextendedreader Partialmatch
slug: dotnet_adsextendedreader_partialmatch
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_partialmatch.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3e0e567b999d368c53dc2bccebfa47b8df1f87f7
---

# Dotnet Adsextendedreader Partialmatch

AdsExtendedReader.PartialMatch

AdsExtendedReader.PartialMatch

Advantage .NET Data Provider

| AdsExtendedReader.PartialMatch  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the Partial Match property used by SetRange, Seek and Filter.

public bool PartialMatch{ get; set; }

Remarks

This property controls the behavior of SetRange, Seek, and Filter. The default value is true.

For Filter, if partial match is true, string comparisons with certain relational operators will ignore trailing spaces. See the Relational Operators section of [Expression Engine Operators](master_expression_engine_operators.md) for details.

For Seek, PartialMatch allows partial matching of a scope or seek value. For example, a Seek on a last name index with a seek value of "Smit" would fail to find "Smith" if PartialMatch is false, but succeed if PartialMatch is true.

Similarly for SetRange, a bottom scope of "S" would exclude "Smith" if PartialMatch is false, but will include all lastnames beginning with "S" if PartialMatch is true.

See Also

[SetRange](dotnet_adsextendedreader_setrange.md)

[Seek](dotnet_adsextendedreader_seek.md)

[Filter](dotnet_adsextendedreader_filter.md)
