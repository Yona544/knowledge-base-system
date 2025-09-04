---
title: Ade Storeactive
slug: ade_storeactive
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_storeactive.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8f246eb8dbd70ddc790ebf817375ae99e2441b68
---

# Ade Storeactive

StoreActive

TAdsDataSet.StoreActive

Advantage TDataSet Descendant

| TAdsDataSet.StoreActive  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md) [TAdsStoredProc](ade_tadsstoredproc.md)

Syntax

property StoreActive: Boolean read FbStoreActive write FbStoreActive;

Description

The StoreActive property specifies whether or not the Active property is written to the DFM file when the form is saved.

The default value of the StoreActive property is True.

If you prefer the Active property never be saved with a form, create a TAdsTable/TAdsQuery/TAdsStoredProc descendant and set the FbStoreActive member variable to False in the constructor.

See Also

[StoreConnected](ade_storeconnected.md)
