---
title: Dotnet Adsdatareader Getvalues
slug: dotnet_adsdatareader_getvalues
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getvalues.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 27d9a18f9824403b901c18397dce9908e4a26f5e
---

# Dotnet Adsdatareader Getvalues

AdsDataReader.GetValues

AdsDataReader.GetValues

Advantage .NET Data Provider

| AdsDataReader.GetValues  Advantage .NET Data Provider |  |  |  |  |

Get all values for the current row.

public int GetValues( object[] values );

Remarks

This method returns the number of instances filled in the object array. For most applications, this method provides an efficient means for retrieving all columns, rather than retrieving each column individually.

You can pass an object array that contains fewer than the number of columns contained in the resulting row. Only the amount of data the object array holds is copied to the array. You can also pass an object array whose length is more than the number of columns contained in the resulting row. This method returns DBNull.Value for null database columns

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)
