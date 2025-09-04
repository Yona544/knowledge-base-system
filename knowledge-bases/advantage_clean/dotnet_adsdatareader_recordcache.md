---
title: Dotnet Adsdatareader Recordcache
slug: dotnet_adsdatareader_recordcache
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_recordcache.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 24379833ff19b1a0f09685e7cc1b9d01e96af4f4
---

# Dotnet Adsdatareader Recordcache

AdsDataReader.RecordCache

AdsDataReader.RecordCache

Advantage .NET Data Provider

| AdsDataReader.RecordCache  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the read-ahead record cache size for the AdsDataReader.

public short RecordCache { get; set; }

Remarks

This property provides access to the read-ahead record cache size. The default value is 100, which works well for reading data sets in one direction. For example, filling a data adapter from an AdsDataReader reads the entire result set in a forward-only direction, and the default cache size provides the best performance.

See [Read-Ahead Record Caching](master_read_ahead_record_caching.md) for more information.
