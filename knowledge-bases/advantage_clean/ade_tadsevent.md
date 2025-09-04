---
title: Ade Tadsevent
slug: ade_tadsevent
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e808e89b204c51cef169eea3470d5e53581b605c
---

# Ade Tadsevent

TAdsEvent

TAdsEvent

Advantage TDataSet Descendant

| TAdsEvent  Advantage TDataSet Descendant |  |  |  |  |

| [Properties](ade_tadsevent_properties.md) | [Events](ade_tadsevent_events.md) |

The TAdsEvent component provides a client side encapsulation of the Advantage Database Server's notification functionality. See [Events (Notifications)](master_events_notifications_.md) for details.

Unit

AdsEventHandler

 

Description

Use TAdsEvent to enable notifications in your application. TAdsEvent creates a background thread and waits for notifications of any of the assigned events. If any configured event is signaled, the assigned OnNotification event is fired. The notification thread creates its own internal TAdsConnection for use, so waiting on an event will not block the main thread of the application.

TAdsEvent clones the AdsConnection component it points to, which means any property changes to the AdsConnection instance will not be reflected in the connection the TAdsEvent component is using until the [TAdsEvent.Active](ade_tadsevent_active.md) property is cycled to false and back to true.
