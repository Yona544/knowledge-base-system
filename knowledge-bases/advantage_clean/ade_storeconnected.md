---
title: Ade Storeconnected
slug: ade_storeconnected
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_storeconnected.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 745ff7374150749789a42100c6f113929f721ca1
---

# Ade Storeconnected

StoreConnected

TAdsConnection.StoreConnected

Advantage TDataSet Descendant

| TAdsConnection.StoreConnected  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Syntax

property StoreConnected : Boolean read FbStoreConnected write FbStoreConnected default TRUE;

Description

The StoreConnected property specifies whether or not the TAdsConnection.IsConnected property is written to the DFM file when the form is saved.

The default value of the StoreConnected property is True.

If you prefer the IsConnected property never be saved with a form, create a TAdsConnection descendant and set the FbStoreConnected member variable to False in the constructor.

See Also

[StoreActive](ade_storeactive.md)
