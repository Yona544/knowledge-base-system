---
title: Ade Adsconnection
slug: ade_adsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a410538a3545c161e33df9088829b281b7e04669
---

# Ade Adsconnection

AdsConnection

TAdsTable/TAdsQuery.AdsConnection

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsConnection  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

A reference to a TAdsConnection component instance.

Syntax

property AdsConnection: TAdsConnection;

Description

The AdsConnection property is used to associate a TAdsTable or TAdsQuery component with a TAdsConnection component, which is used to manage Advantage server connections.

This property can be used in place of the [DatabaseName](ade_databasename.md) property. It is more efficient and it is thread-safe.

When writing multi-threaded applications, or libraries that will be consumed by multi-threaded applications, it is more efficient and thread-safe to use the AdsConnection property instead of the DatabaseName property. Assigning the pointer to the AdsConnection directly is safer than relying on the name resolution logic used when setting the DatabaseName property.
