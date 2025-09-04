---
title: Ade Adsgetrecordlength
slug: ade_adsgetrecordlength
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetrecordlength.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 66a1d2e08381d1749fe5a1717b697f2446dcba2d
---

# Ade Adsgetrecordlength

AdsGetRecordLength

TAdsTable.AdsGetRecordLength

Advantage TDataSet Descendant

| TAdsTable.AdsGetRecordLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the record size for the given table.

Syntax

function AdsGetRecordLength : Longint;

Description

The record size returned includes space for the deleted byte for DBF table records. For ADT records, this record size will include 5 extra bytes used internally by Advantage. This length may not reflect the actual amount of data accessible for this record if the table includes variable-length fields.

Example

AdsTable1.Active := TRUE;

lRecordCount := AdsTable1.AdsGetRecordLength;

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.md)
