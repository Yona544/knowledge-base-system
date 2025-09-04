---
title: Ade Tadsevent Active
slug: ade_tadsevent_active
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent_active.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fbebba518a594fd3bb532a39a28aae321483d258
---

# Ade Tadsevent Active

TAdsEvent.Active

TAdsEvent.Active

Advantage TDataSet Descendant

| TAdsEvent.Active  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.md)

Defines whether the event listener is active.

Syntax

property Active: Boolean;

Description

When the true, the listener will wait for the associated event(s) to be signaled.

When set to false, TAdsEvent will terminate its background thread that is waiting on events. This thread termination is synchronous and can take up to 2 seconds, depending on the [EventTimeout](ade_tadsevent_eventtimeout.md) property setting. If the EventTimeout setting is -1, or over 2000, it can take 2 full seconds to terminate the thread. If EventTimeout is less than 2000, the thread can be terminated in the same number of milliseconds as EventTimeout specifies. When using the Advantage Local Server the thread can be terminated in the same number of milliseconds as the [PollInterval](ade_tadsevent_pollinterval.md) property specifies.
