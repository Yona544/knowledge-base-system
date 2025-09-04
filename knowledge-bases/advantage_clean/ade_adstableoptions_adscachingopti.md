---
title: Ade Adstableoptions Adscachingopti
slug: ade_adstableoptions_adscachingopti
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adstableoptions_adscachingopti.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f64ed3e2d87d22defa8685d8eafa2978771c5082
---

# Ade Adstableoptions Adscachingopti

AdsTableOptions.AdsCachingOption

AdsTableOptions.AdsCachingOption

Advantage TDataSet Descendant

| AdsTableOptions.AdsCachingOption  Advantage TDataSet Descendant |  |  |  |  |

Indicates the caching mode of the table.

Syntax

type TAdsTableCachingOption = ( tcNone, tcReads, tcWrites );

property AdsTableOptions.AdsCachingOption

Description

Caching mode to use.  tcNone is the default option and doesnt enable any caching.  tcReads enables caching of table data for reads only.  Updates to the table still get written to the disk.  tcWrites enables read and write caching.  Updates get written to the cache in memory and are only written to disk when the table is closed.  See [Table Data Caching](master_table_data_caching.md) for more information.

See Also

[Table Data Caching](master_table_data_caching.md)
