---
title: Dotnet Adsextendedreader Writerecord
slug: dotnet_adsextendedreader_writerecord
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_writerecord.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ad53957ee7d46e6d3a6f079209782cf02db93354
---

# Dotnet Adsextendedreader Writerecord

AdsExtendedReader.WriteRecord

AdsExtendedReader.WriteRecord

Advantage .NET Data Provider

| AdsExtendedReader.WriteRecord  Advantage .NET Data Provider |  |  |  |  |

Writes any changes in the current record.

public void WriteRecord();

Remarks

WriteRecord flushes any data changes to the Advantage server. If an implicit lock is held on the record, calling this function will release it.
