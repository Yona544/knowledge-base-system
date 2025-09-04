---
title: Dotnet Adsextendedreader Indexcondition
slug: dotnet_adsextendedreader_indexcondition
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_indexcondition.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2ed3e24dcc9cc44710dce0c0c0336d0c3be9848d
---

# Dotnet Adsextendedreader Indexcondition

AdsExtendedReader.IndexCondition

AdsExtendedReader.IndexCondition

Advantage .NET Data Provider

| AdsExtendedReader.IndexCondition  Advantage .NET Data Provider |  |  |  |  |

Get the condition associated with the active index.

public string IndexCondition{ get; }

Remarks

This property returns the conditional expression for the active index if the index was created with a condition. If not, the property value will be an empty (0 length) string.

See Also

[AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.md)

[AdsExtendedReader.CreateIndex](dotnet_adsextendedreader_createindex.md)

[AdsExtendedReader.IndexExpression](dotnet_adsextendedreader_indexexpression.md)
