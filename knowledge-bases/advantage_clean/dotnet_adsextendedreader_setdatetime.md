---
title: Dotnet Adsextendedreader Setdatetime
slug: dotnet_adsextendedreader_setdatetime
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setdatetime.htm
source: Advantage CHM
tags:
  - dotnet
checksum: f7aa6ccbc1a19a8ae8dda2a7efcc38bdda161d6e
---

# Dotnet Adsextendedreader Setdatetime

AdsExtendedReader.SetDateTime

AdsExtendedReader.SetDateTime

Advantage .NET Data Provider

| AdsExtendedReader.SetDateTime  Advantage .NET Data Provider |  |  |  |  |

Stores the given DateTime value as a date or timestamp in the specified column.

public void SetDateTime( int iCol, DateTime value );

Remarks

This method sets the specified zero-based column value to the given DateTime value. SetDateTime is expected when setting fields of types date of timestamp. No conversions are performed. To set a date or timestamp field to NULL, use SetValue with a null or empty value.

Note The time portion of the DataTime is ignored for date fields.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.md)

[AdsDataReader.GetDateTime](dotnet_adsdatareader_getdatetime.md)
