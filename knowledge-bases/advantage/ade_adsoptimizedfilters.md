AdsOptimizedFilters




Advantage Database Server 12  

AdsTableOptions.AdsOptimizedFilters

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsOptimizedFilters  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsOptimizedFilters Advantage TDataSet Descendant ade\_Adsoptimizedfilters Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsOptimizedFilters  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Indicates whether or not to use the Advantage Optimized Filters.

Syntax

property AdsTableOptions.AdsOptimizedFilters;

Description

This property indicates whether or not to use the Advantage Optimized Filters and affects how the filter property is implemented. By default this is True.

[Advantage Optimized Filters](master_advantage_optimized_filters.htm) (AOFs) provide state of the art filter optimization for Advantage Client Engine applications. AOFs speed filter processing by using index keys instead of table records. If a specified field has an index built on it, then an AOF uses the index file rather than the table to process the query. Performance is increased by reducing the amount of data that must be retrieved from the disk.

Note By setting this property to True, AOFs will be used for any procedures, functions, methods, or properties that use filters.