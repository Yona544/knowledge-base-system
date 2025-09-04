---
title: Master Sp Dropallevents
slug: master_sp_dropallevents
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_dropallevents.htm
source: Advantage CHM
tags:
  - master
checksum: 5ce704ecb19d931a280dde5102d70f1adde204a3
---

# Master Sp Dropallevents

sp\_DropAllEvents

sp\_DropAllEvents

Advantage SQL Engine

| sp\_DropAllEvents  Advantage SQL Engine |  |  |  |  |

This procedure removes all events for the connection.

Syntax

sp\_DropAllEvents( Options, integer );

Parameters

| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |

See Also

[sp\_CreateEvent](master_sp_createevent.md)

[sp\_DropEvent](master_sp_dropevent.md)

[sp\_SignalEvent](master_sp_signalevent.md)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.md)

[sp\_WaitForEvent](master_sp_waitforevent.md)

Example

EXECUTE PROCEDURE sp\_DropAllEvents( 0 );
