---
title: Dotnet Adsparameter Index
slug: dotnet_adsparameter_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_index.htm
source: Advantage CHM
tags:
  - dotnet
checksum: bfe9a0abbc570a2685952bd19f494dc0676781d9
---

# Dotnet Adsparameter Index

AdsParameter.Index

AdsParameter.Index

Advantage .NET Data Provider

| AdsParameter.Index  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the one-based parameter index number of unnamed parameters.

public int Index { get; set; }

Remarks

When using unnamed parameters (represented by a question mark) in an SQL statement, the AdsParameter.Index property should be set to the one-based ordinal of the parameter as it appears in the SQL statement.
