---
title: Ade Tadsevent Adsconnection
slug: ade_tadsevent_adsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent_adsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 18339a2ea145d96abbefba2ddaf0272d244f826e
---

# Ade Tadsevent Adsconnection

TAdsEvent.AdsConnection

TAdsEvent.AdsConnection

Advantage TDataSet Descendant

| TAdsEvent.AdsConnection  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.md)

A reference to the connection this event should clone.

Syntax

property AdsConnection: TAdsConnection;

Description

The AdsConnection property is used to provide the TAdsEvent component with the connection details to be used for Advantage connections.  The TAdsEvent component will instantiate an AdsConnection component for internal use, cloning all appropriate properties from the provided AdsConnection instance.
