---
title: Ade Filter
slug: ade_filter
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_filter.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0281586e80893a806814cb72e1750d52015b38e7
---

# Ade Filter

Filter

TAdsDataSet.Filter

Advantage TDataSet Descendant

| TAdsDataSet.Filter  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsStoredProc](ade_tadsstoredproc.md)

Specifies the filter expression string for the given dataset.

Syntax

property Filter: string;

Description

Use Filter to specify a dataset filter. When filtering is applied to a dataset, only those records that meet a filters conditions are available to an application. Filter contains the string that describes the filter condition.

Starting with Advantage version 5.5, exact match is the default. Unless the '\*' character is used at the end of the filter, the result will be an exact match. To set a filter based on a partial comparison, use the \* character to specify the partial string to filter. For example:

Lastname = Co\*; // This will include all Lastnames that begin Co

To create a filter that will find an exact match, do not include the \* character in the filter string. For example:

Lastname = Smith; // This will not include the lastnames that start with Smith like Smithers

For additional information about the proper filter strings for different data types, visit the Advantage Developer Zone Web site, http://DevZone.AdvantageDatabase.com, and download an example application from the "Downloads" area in the "Delphi" section that covers the most common topics in Advantage/Delphi programming.

See Also

[AdsTableOptions.AdsAOFResolveImmediate](ade_adsaofresolveimmediate.md)

[AdsTableOptions.AdsFilterOptions](ade_adsfilteroptions.md)

[AdsTableOptions.AdsOptimizedFilters](ade_adsoptimizedfilters.md)

[AdsTableOptions.AdsAOFType](ade_adsaoftype.md)
