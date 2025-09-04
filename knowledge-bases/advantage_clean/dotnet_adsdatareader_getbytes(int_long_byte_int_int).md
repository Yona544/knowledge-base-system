---
title: Dotnet Adsdatareader Getbytes(Int Long Byte Int Int)
slug: dotnet_adsdatareader_getbytes(int_long_byte_int_int)
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getbytes(int_long_byte_int_int).htm
source: Advantage CHM
tags:
  - dotnet
checksum: 23272a4a0795cb96f07bcb3ab350b6a5a6ed9d73
---

# Dotnet Adsdatareader Getbytes(Int Long Byte Int Int)

AdsDataReader.GetBytes(int, long, byte[], int, int)

AdsDataReader.GetBytes(int, long, byte[ ], int, int)

Advantage .NET Data Provider

| AdsDataReader.GetBytes(int, long, byte[ ], int, int)  Advantage .NET Data Provider |  |  |  |  |

Reads a stream of bytes from the specified column offset into the buffer an array starting at the given buffer offset.

public long GetBytes

(

int iCol, // (I) 0-based column index

long lFieldOffset, // (I) offset to start reading from

byte[] buffer, // (O) output buffer

int iBufferOffset,// (I) starting offset in output buffer

int iLength // (I) number of bytes to read

);

Return Value

The actual number of bytes read.

Remarks

If you pass a buffer that is a null reference (Nothing in Visual Basic), GetBytes returns the length of the field in bytes.

No conversions are performed; therefore the data retrieved must already be a byte array. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)

[GetBytes()](dotnet_adsdatareader_getbytes().htm)
