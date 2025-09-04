---
title: Dotnet Adsextendedreader Setboolean
slug: dotnet_adsextendedreader_setboolean
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setboolean.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c96f354d12c464ee3be7ea90be1079febde0f8d4
---

# Dotnet Adsextendedreader Setboolean

AdsExtendedReader.SetBoolean

AdsExtendedReader.SetBoolean

Advantage .NET Data Provider

| AdsExtendedReader.SetBoolean  Advantage .NET Data Provider |  |  |  |  |

Stores the given boolean value in the specified column.

public void SetBoolean( int iCol, bool value );

Remarks

This method sets the specified zero-based column value to true or false. No conversions are performed. To set a boolean field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetBoolean](dotnet_adsdatareader_getboolean.md)
