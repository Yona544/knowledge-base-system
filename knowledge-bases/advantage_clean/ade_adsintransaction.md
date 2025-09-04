---
title: Ade Adsintransaction
slug: ade_adsintransaction
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsintransaction.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6ba04b2bb8523a64b6e90d1ca0994b48763dee85
---

# Ade Adsintransaction

AdsInTransaction

TAdsTable/TAdsQuery.AdsInTransaction

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsInTransaction  Advantage TDataSet Descendant |  |  |  |  |

Tests if the dataset is within a transaction.

Syntax

function AdsInTransaction: boolean;

Description

AdsInTransaction will return True if this dataset is currently within a transaction and False otherwise.

Example

{ start a transaction for all records associated with AdsConnection1 }

AdsConnection1.BeginTransaction;

 

{ is this table in a transaction, It should be if it is associated to AdsConnection1 }

bInTransaction := AdsTable1.AdsInTransaction;

See Also

None.
