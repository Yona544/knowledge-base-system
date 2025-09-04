---
title: Dotnet Adsdatareader Getvalue
slug: dotnet_adsdatareader_getvalue
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getvalue.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2afa07f8b4307084b50b49c6b87c7adbd47a551f
---

# Dotnet Adsdatareader Getvalue

AdsDataReader.GetValue

AdsDataReader.GetValue

Advantage .NET Data Provider

| AdsDataReader.GetValue  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column in its native format.

public object GetValue( int columnNumber );

Remarks

This method retrieves the specified zero-based column value in the native format. This method returns DBNull.Value for null database columns.

See Also

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
