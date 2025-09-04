---
title: Ade Adsrefreshrecord
slug: ade_adsrefreshrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsrefreshrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8cf4d986e8798f417d698b762ff264be2eda6640
---

# Ade Adsrefreshrecord

AdsRefreshRecord

TAdsTable.AdsRefreshRecord

Advantage TDataSet Descendant

| TAdsTable.AdsRefreshRecord  Advantage TDataSet Descendant |  |  |  |  |

Rereads the current record.

Syntax

procedure AdsRefreshRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: Refresh. See your Delphi documentation for more information about this native Delphi method.

Description

Rereads the record from the server. This function should be used if it is likely that another concurrent user has updated the record this user is currently positioned on. When it is not possible for another user to update the record (the record is locked, the table is locked, or the table is opened exclusively) this function will do nothing. To cancel an update, use AdsCancelUpdate.

Example

AdsTable1.Refresh;

See Also

[AdsLockRecord](ade_adslockrecord.md)
