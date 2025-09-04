---
title: Dotnet Adsextendedreader Clearrange
slug: dotnet_adsextendedreader_clearrange
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_clearrange.htm
source: Advantage CHM
tags:
  - dotnet
checksum: b29a0985d35b08d0ef158cb4311e9ab4f7034269
---

# Dotnet Adsextendedreader Clearrange

AdsExtendedReader.ClearRange

AdsExtendedReader.ClearRange

Advantage .NET Data Provider

| AdsExtendedReader.ClearRange  Advantage .NET Data Provider |  |  |  |  |

Clears top and bottom range values on the index order.

public void ClearRange();

Remarks

This method clears both the top and bottom range values on the active index order. After calling this method, the reader will be positioned at BOF (beginning of file) so that a call to Read() will then go to the first record.

See Also

[SetRange](dotnet_adsextendedreader_setrange.md)
