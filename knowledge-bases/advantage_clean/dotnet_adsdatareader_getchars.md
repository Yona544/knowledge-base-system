---
title: Dotnet Adsdatareader Getchars
slug: dotnet_adsdatareader_getchars
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getchars.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ccfad2c670a0f0b64a72d8e7093e09d2035fd20f
---

# Dotnet Adsdatareader Getchars

AdsDataReader.GetChars

AdsDataReader.GetChars

Advantage .NET Data Provider

| AdsDataReader.GetChars  Advantage .NET Data Provider |  |  |  |  |

Reads a stream of characters from the specified column offset into the buffer as an array starting at the given buffer offset.

public long GetChars

(

int iCol, // (I) 0-based column index

long lFieldOffset, // (I) offset to start reading from

char[] buffer, // (O) output buffer

int iBufferOffset,// (I) starting offset in output buffer

int iLength // (I) number of bytes to read

);

Return Value

The actual number of characters read.

Remarks

If you pass a buffer that is a null reference (Nothing in Visual Basic), GetChars returns the length of the field in characters.

No conversions are performed; therefore the data retrieved must already be a character array (memo or string field). This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

Note This method is not affected by the TrimTrailingSpaces option (see [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)).

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
