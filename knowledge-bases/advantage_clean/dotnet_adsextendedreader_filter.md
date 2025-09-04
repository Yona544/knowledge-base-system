---
title: Dotnet Adsextendedreader Filter
slug: dotnet_adsextendedreader_filter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_filter.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 27dc32d14ac9baf92cd6b2722872fe2e491986fb
---

# Dotnet Adsextendedreader Filter

AdsExtendedReader.Filter

AdsExtendedReader.Filter

Advantage .NET Data Provider

| AdsExtendedReader.Filter  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the Advantage Optimized Filter expression.

public string Filter{ get; set; }

Remarks

Retrieves or sets the Advantage Optimized Filter (AOF). Setting Filter to an empty string will clear the filter. For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

After setting or clearing a filter, the reader will be positioned at BOF (beginning of file) so that a call to Read() will then go to the first record.
