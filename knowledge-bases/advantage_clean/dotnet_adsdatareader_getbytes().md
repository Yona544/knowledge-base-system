---
title: Dotnet Adsdatareader Getbytes()
slug: dotnet_adsdatareader_getbytes()
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getbytes().htm
source: Advantage CHM
tags:
  - dotnet
checksum: f6d2323d2f2d43d8fe3764bc35c48c6639e065c7
---

# Dotnet Adsdatareader Getbytes()

AdsDataReader.GetBytes()

AdsDataReader.GetBytes()

Advantage .NET Data Provider

| AdsDataReader.GetBytes()  Advantage .NET Data Provider |  |  |  |  |

Retrieves a binary or raw field as an array of bytes.

public byte[] GetBytes( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as an array of bytes. No conversions are performed; therefore the data retrieved must already be a byte array (raw field or BLOB field). This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)

[GetBytes(int, long, byte[], int, int)](dotnet_adsdatareader_getbytes(int_long_byte_int_int).htm)
