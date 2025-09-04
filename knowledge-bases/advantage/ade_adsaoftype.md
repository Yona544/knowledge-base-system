AdsAOFType




Advantage Database Server 12  

AdsTableOptions.AdsAOFType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsAOFType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsAOFType Advantage TDataSet Descendant ade\_Adsaoftype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsAOFType  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Specifies what type of AOF to use. Different AOF types provide different levels of filter membership.

Syntax

property AdsTableOptions.AdsAOFType

Description

|  |  |
| --- | --- |
| atDynamic: | Filter membership is affected by modifications all users make to record data. Note: Dynamic filters are only supported when connected to the Advantage Database Server. If using the Advantage Local Server, dynamic filters will behave like keyset filters. |
| atKeySet: | Filter membership is only affected by updates from the filter owner (the table instance that set the filter). Updates made by other users will not affect a records membership in the filter unless another user modifies a record so that it no longer meets the filter condition and the filter owner refreshes that record. The refresh operation will cause a re-evaluation of the filter expression and the record will be removed from the filter. |
| atFixed: | Filter membership does not change. If other users modify records they will always remain visible within this fixed filter, even if the changes have modified field values such that the record no longer passes the original filter expression. |

See Also

[AdsTableOptions.AdsFilterOptions](ade_adsfilteroptions.htm)

[AdsTableOptions.AdsOptimizedFilters](ade_adsoptimizedfilters.htm)