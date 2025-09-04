---
title: Dotnet Adsdatareader Fieldcount
slug: dotnet_adsdatareader_fieldcount
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_fieldcount.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 7ce00ad2b8b4a040cce2a8f50b627a433eff4172
---

# Dotnet Adsdatareader Fieldcount

AdsDataReader.FieldCount

AdsDataReader.FieldCount

Advantage .NET Data Provider

| AdsDataReader.FieldCount  Advantage .NET Data Provider |  |  |  |  |

Gets the number of columns contained in the result set.

public int FieldCount { get; }

Remarks

When not positioned in a valid recordset, this property returns 0; otherwise it returns the number of columns in the result set. The default is -1. After executing a query that does not return rows, FieldCount returns -1.
