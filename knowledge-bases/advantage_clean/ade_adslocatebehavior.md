---
title: Ade Adslocatebehavior
slug: ade_adslocatebehavior
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adslocatebehavior.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f5a0edf4592d04f6536ce1e6bec87d5850427440
---

# Ade Adslocatebehavior

AdsLocateBehavior

AdsTableOptions.AdsLocateBehavior

Advantage TDataSet Descendant

| AdsTableOptions.AdsLocateBehavior  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Controls the behavior of the Locate method.

Syntax

type TAdsLocateBehavior = ( lbFastestPossible, lbFindFirst );

 

property AdsTableOptions.AdsLocateBehavior;

Description

This property controls the behavior of the Locate method for TAdsTable and TAdsQuery objects. The default is lbFastestPossible. The setting of this property affects which record may be located when more than one record matches the values given to the Locate method. For example, the call adsTable.Locate('state', 'WA', []); could potentially match multiple records. The AdsLocateBehavior option can be used to control which record will be the active record after the call.

When the property is set to lbFastestPossible, the Locate method will use an indexed seek operation if possible. If the fields specified in the Locate call do not match the active index or if there is no active index, then it is not guaranteed that the resulting active record will be the first one in the record set order that matches (if there are multiple matching records). This is because a seek operation finds the first matching entry in the index order that is used for the seek. If that order is different from corresponding order of the active index, then the record will not be the first one in the active order.

When the property is set to lbFindFirst, it guarantees that the active record after the Locate call will be the first one in the current order of the result set. When using this setting, the Locate method will use a seek operation only if the locate fields correspond to the active index. If there is no active index or if the Locate call specifies fields that do not match the current index, the Locate method will set a filter (e.g., an AOF) to perform the operation. As a result, the Locate call may be slower when this option is used particularly if the result set has an active index. There is more overhead involved when setting a filter versus performing a seek operation.
