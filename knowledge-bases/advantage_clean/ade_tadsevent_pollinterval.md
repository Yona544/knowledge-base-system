---
title: Ade Tadsevent Pollinterval
slug: ade_tadsevent_pollinterval
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tadsevent_pollinterval.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6ae9e9d76f42e7599db14e875f9109b52d935ba2
---

# Ade Tadsevent Pollinterval

TAdsEvent.PollInterval

TAdsEvent.PollInterval

Advantage TDataSet Descendant

| TAdsEvent.PollInterval  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.md)

Used to specify the interval between polls of the shared events table when waiting for the event.

Syntax

property PollInterval: Integer

Description

Only used for local server connections.  The PollInterval is used to specify the interval between polls of the shared events table when waiting for the event.  Zero can be specified to use a default interval (which is currently 300 milliseconds).

See Also

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.md)
