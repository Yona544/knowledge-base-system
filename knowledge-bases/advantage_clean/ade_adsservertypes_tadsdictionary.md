---
title: Ade Adsservertypes Tadsdictionary
slug: ade_adsservertypes_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsservertypes_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a7d45e7ef3a5bc4d1287e8c23ed95888fae4e06e
---

# Ade Adsservertypes Tadsdictionary

AdsServerTypes

TAdsDictionary.AdsServerTypes

Advantage TDataSet Descendant

| TAdsDictionary.AdsServerTypes  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Defines the Advantage server types to which this connection may attempt to connect.

Syntax

property AdsServerTypes : TAdsServerTypes;

 

TAdsServerTypes = set of TAdsServerType

TAdsServerType = ( stADS\_REMOTE, stADS\_LOCAL, stADS\_AIS )

Description

The Advantage server connection for this TAdsDictionary component will only attempt to use the server types indicated in the set.
