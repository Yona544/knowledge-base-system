---
title: Ade Adsservertypes Adsconnection
slug: ade_adsservertypes_adsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsservertypes_adsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 564ecfe169e918534d4f84ea4a09d7318c1f5d5e
---

# Ade Adsservertypes Adsconnection

AdsServerTypes

TAdsConnection.AdsServerTypes

Advantage TDataSet Descendant

| TAdsConnection.AdsServerTypes  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Defines the Advantage server types to which this connection may attempt to connect.

Syntax

property AdsServerTypes : TAdsServerTypes;

 

TAdsServerTypes = set of TAdsServerType

TAdsServerType = ( stADS\_REMOTE, stADS\_LOCAL, stADS\_AIS )

Description

This property overrides the TAdsSettings.AdsServerTypes value if the application has a TAdsSettings component. The Advantage server connection for this TAdsConnection component will only attempt to use the server types indicated in the set. If this set is empty, the default, then the TAdsSettings.AdsServerTypes property set will be used.

See [TAdsSettings.AdsServerTypes](ade_adsservertypes_adssettings.md) for a full explanation.
