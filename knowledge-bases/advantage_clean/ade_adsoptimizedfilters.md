---
title: Ade Adsoptimizedfilters
slug: ade_adsoptimizedfilters
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsoptimizedfilters.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f903334b2b9299e7ba0a1f8a3f659e3ee61b0eca
---

# Ade Adsoptimizedfilters

AdsOptimizedFilters

AdsTableOptions.AdsOptimizedFilters

Advantage TDataSet Descendant

| AdsTableOptions.AdsOptimizedFilters  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Indicates whether or not to use the Advantage Optimized Filters.

Syntax

property AdsTableOptions.AdsOptimizedFilters;

Description

This property indicates whether or not to use the Advantage Optimized Filters and affects how the filter property is implemented. By default this is True.

[Advantage Optimized Filters](master_advantage_optimized_filters.md) (AOFs) provide state of the art filter optimization for Advantage Client Engine applications. AOFs speed filter processing by using index keys instead of table records. If a specified field has an index built on it, then an AOF uses the index file rather than the table to process the query. Performance is increased by reducing the amount of data that must be retrieved from the disk.

Note By setting this property to True, AOFs will be used for any procedures, functions, methods, or properties that use filters.
