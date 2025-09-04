---
title: Dotnet Adsextendedreader Setchars
slug: dotnet_adsextendedreader_setchars
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setchars.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 75f73f8a506c10fd6fb8768e35f2378fb688ba6e
---

# Dotnet Adsextendedreader Setchars

AdsExtendedReader.SetChars

AdsExtendedReader.SetChars

Advantage .NET Data Provider

| AdsExtendedReader.SetChars  Advantage .NET Data Provider |  |  |  |  |

Stores the characters of the given character array in the specified column.

public void SetChars( int iCol, char[] value );

Remarks

This method sets the specified zero-based column value to the characters of the given character array. SetChars may be used for numeric, string, memo or varchar types. No conversions are performed. To set a variable length character field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetChars](dotnet_adsdatareader_getchars.md)
