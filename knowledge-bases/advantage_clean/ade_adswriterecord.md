---
title: Ade Adswriterecord
slug: ade_adswriterecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adswriterecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 541127ca705a2a88aa809677cb4276a0734334c3
---

# Ade Adswriterecord

AdsWriteRecord

TAdsTable.AdsWriteRecord

Advantage TDataSet Descendant

| TAdsTable.AdsWriteRecord  Advantage TDataSet Descendant |  |  |  |  |

Writes any changes in the current record.

Syntax

procedure AdsWriteRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: Post. See your Delphi documentation for more information about this native Delphi method.

Description

AdsWriteRecord flushes any data changes to the servers disk. If an implicit lock is held on the record, calling this function will release it.

Example

AdsTable1.Append;

AdsTable1.FieldByName( LastName ).AsString := Smith;

AdsTable1.Post;

See Also

None.
