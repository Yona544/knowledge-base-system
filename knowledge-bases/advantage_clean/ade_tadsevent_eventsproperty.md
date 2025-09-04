---
title: Ade Tadsevent Eventsproperty
slug: ade_tadsevent_eventsproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent_eventsproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 65d648f3e761d4ce91346f0cd6852b838919c851
---

# Ade Tadsevent Eventsproperty

TAdsEvent.EventsProperty

TAdsEvent.Events

Advantage TDataSet Descendant

| TAdsEvent.Events  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.md)

A case insensitive list of the events this component should listen to.

Syntax

property Events: TStrings

Description

The Events property is used to define a case-insensitive list of event names for which the component should wait.  The component will create each event via the sp\_CreateEvent stored procedure, then wait for each of the events to be signaled.
