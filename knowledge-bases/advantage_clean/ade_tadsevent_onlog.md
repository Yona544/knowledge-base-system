---
title: Ade Tadsevent Onlog
slug: ade_tadsevent_onlog
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent_onlog.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: dceafd1059e992781acb134df2a267010da4e5b5
---

# Ade Tadsevent Onlog

TAdsEvent.OnLog

TAdsEvent.OnLog

Advantage TDataSet Descendant

| TAdsEvent.OnLog  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.md)

OnLog occurs when debug information is available.

Syntax

type TAdsLogEvent = procedure ( Sender : TObject;

                               log : String ) of object;

property OnLog : TAdsLogEvent;

Description

Write an OnLog event handler to receive debug information about internal activities and any exceptions that may occur in the TAdsEvent component.

This event is called using the TThread.Synchronize method, which means the main Delphi VCL thread will not be able to interact with the user interface while executing this event. The OnLog event handler should be kept short and efficient.
