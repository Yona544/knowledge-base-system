---
title: Ade Tadsevent Onnotification
slug: ade_tadsevent_onnotification
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent_onnotification.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 39e7cf22d1dbce9f168473581c1298742c0f6df7
---

# Ade Tadsevent Onnotification

TAdsEvent.OnNotification

TAdsEvent.OnNotification

Advantage TDataSet Descendant

| TAdsEvent.OnNotification  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.md)

OnNotification occurs when any configured event is signalled.

Syntax

type TAdsNotifyEvent = procedure ( Sender : TObject;

                                  event : String;

                                  count : Integer;

                                  eventdata : String ) of object;   
property OnNotification : TAdsNotifyEvent;

Parameters

Sender:  Object reference of the event sender

Event : Name of the event that was signaled

Count : Number of times the event has been signaled

EventData : Any data returned by the event signal

 

Description

Write an OnNotification event handler to take appropriate actions within your application when a configured notification is signaled.

This event is called using the TThread.Synchronize method, which means the main Delphi VCL thread will not be able to interact with the user interface while executing this event. The OnLog event handler should be kept short and efficient.
