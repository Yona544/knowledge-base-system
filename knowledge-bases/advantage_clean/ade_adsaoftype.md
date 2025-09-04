---
title: Ade Adsaoftype
slug: ade_adsaoftype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsaoftype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9d4aeb60d97fdb8241824592e98079e80a7b1c4a
---

# Ade Adsaoftype

AdsAOFType

AdsTableOptions.AdsAOFType

Advantage TDataSet Descendant

| AdsTableOptions.AdsAOFType  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Specifies what type of AOF to use. Different AOF types provide different levels of filter membership.

Syntax

property AdsTableOptions.AdsAOFType

Description

| atDynamic: | Filter membership is affected by modifications all users make to record data. Note: Dynamic filters are only supported when connected to the Advantage Database Server. If using the Advantage Local Server, dynamic filters will behave like keyset filters. |
| atKeySet: | Filter membership is only affected by updates from the filter owner (the table instance that set the filter). Updates made by other users will not affect a records membership in the filter unless another user modifies a record so that it no longer meets the filter condition and the filter owner refreshes that record. The refresh operation will cause a re-evaluation of the filter expression and the record will be removed from the filter. |
| atFixed: | Filter membership does not change. If other users modify records they will always remain visible within this fixed filter, even if the changes have modified field values such that the record no longer passes the original filter expression. |

See Also

[AdsTableOptions.AdsFilterOptions](ade_adsfilteroptions.md)

[AdsTableOptions.AdsOptimizedFilters](ade_adsoptimizedfilters.md)
