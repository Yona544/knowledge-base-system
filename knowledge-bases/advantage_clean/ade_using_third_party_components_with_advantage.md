---
title: Ade Using Third Party Components With Advantage
slug: ade_using_third_party_components_with_advantage
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_using_third_party_components_with_advantage.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a389f68a29f43ace16a23254970555dc65d69462
---

# Ade Using Third Party Components With Advantage

Using Third-Party Components with Advantage

Using Third-Party Components with Advantage

Advantage TDataSet Descendant

| Using Third-Party Components with Advantage  Advantage TDataSet Descendant |  |  |  |  |

Advantage TDataSet Descendant

The Advantage TDataSet Descendant is compatible with all data-aware components that ship with Delphi/C++Builder, with the exception of TBatchMove (For TBatchMove functionality see the [TAdsBatchMove](ade_tadsbatchmove.md) component).

For third-party components to work with the Advantage TDataSet Descendant, the component must be engineered to work with a generic TDataSet descendant or standard TDataSource class. This means that the component must not type-cast the dataset to a TTable or any other descendant other than TAdsDataset, TAdsTable, TAdsQuery, or TAdsStoredProc. It also means that the component must not make any direct BDE API function calls (for example DbiGetRecordCount).
