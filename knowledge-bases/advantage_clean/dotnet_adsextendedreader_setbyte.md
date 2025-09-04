---
title: Dotnet Adsextendedreader Setbyte
slug: dotnet_adsextendedreader_setbyte
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setbyte.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2f9a4a22669ebb60b05c70c47599fee43a08d6fe
---

# Dotnet Adsextendedreader Setbyte

AdsExtendedReader.SetByte

AdsExtendedReader.SetByte

Advantage .NET Data Provider

| AdsExtendedReader.SetByte  Advantage .NET Data Provider |  |  |  |  |

Stores the given byte value in the specified column.

public void SetByte( int iCol, byte value);

Remarks

This method sets the specified zero-based column value to the given byte value. No conversions are performed. To set a byte field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetByte](dotnet_adsdatareader_getbyte.md)
