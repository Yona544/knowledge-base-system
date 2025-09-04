---
title: Dotnet Adsextendedreader Readprevious
slug: dotnet_adsextendedreader_readprevious
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_readprevious.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5deae4c4df9d36b2ce8dad464823a56653bd24a0
---

# Dotnet Adsextendedreader Readprevious

AdsExtendedReader.ReadPrevious

AdsExtendedReader.ReadPrevious

Advantage .NET Data Provider

| AdsExtendedReader.ReadPrevious  Advantage .NET Data Provider |  |  |  |  |

Moves to the previous record.

public bool ReadPrevious();

Remarks

This returns true if it successfully positioned to the previous row and False if there are no more rows. If you use this method, [AdsDataReader.RecordCache](dotnet_adsdatareader_recordcache.md) will be changed down to 10 if it is at its original value of 100.

See Also

[AdsDataReader.Read](dotnet_adsdatareader_read.md)

[AdsDataReader.RecordCache](dotnet_adsdatareader_recordcache.md)
