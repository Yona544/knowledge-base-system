---
title: Dotnet Adsextendedreader Seektype
slug: dotnet_adsextendedreader_seektype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_seektype.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c5644dea96f66fcc666864b50e453f6c478ca971
---

# Dotnet Adsextendedreader Seektype

AdsExtendedReader.SeekType

AdsExtendedReader.SeekType

Advantage .NET Data Provider

| AdsExtendedReader.SeekType  Advantage .NET Data Provider |  |  |  |  |

public enum SeekType

Remarks

Indicates if hard or soft seek is used when performing a Seek operation. Use of soft seek allows a record to be found with the next higher key value if the given key does not exist.

| Name | Description |
| SoftSeek | Allows record to be found with the next higher key value if the given key does not exist. |
| HardSeek | Seeks an exact match. |
| SeekLast | Seeks for the last value in an index. |
| SeekGT | Seeks for the next possible index key after the given key. |

See Also

[Seek](dotnet_adsextendedreader_seek.md)
