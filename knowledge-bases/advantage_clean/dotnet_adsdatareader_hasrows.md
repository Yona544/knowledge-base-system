---
title: Dotnet Adsdatareader Hasrows
slug: dotnet_adsdatareader_hasrows
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_hasrows.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ac080eccffb1c2958a5158ce4e7e5710df2f524a
---

# Dotnet Adsdatareader Hasrows

AdsDataReader.HasRows

AdsDataReader.HasRows

Advantage .NET Data Provider

| AdsDataReader.HasRows  Advantage .NET Data Provider |  |  |  |  |

Gets a value indicating whether the data reader has one or more rows.

public bool HasRows{ get; }

Remarks

This returns true if the reader object has at least one row in it when the reader object is created. If it is an empty result set at creation time, this property will be false.

Note that the HasRows property is not updated in response to the addition or deletion of records by the [AdsExtendedReader](dotnet_adsextendedreader.md) object. The intention of this property is to reflect only whether a call to the [Read()](dotnet_adsdatareader_read.md) method will return true for at least one row immediately after creating the reader object.
