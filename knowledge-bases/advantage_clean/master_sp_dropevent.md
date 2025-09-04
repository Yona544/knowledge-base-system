---
title: Master Sp Dropevent
slug: master_sp_dropevent
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_dropevent.htm
source: Advantage CHM
tags:
  - master
checksum: d9416233e179a1aa934a05f6370d4eb722528b8e
---

# Master Sp Dropevent

sp\_DropEvent

sp\_DropEvent

Advantage SQL Engine

| sp\_DropEvent  Advantage SQL Engine |  |  |  |  |

This procedure removes the event for the active connection.

Syntax

sp\_DropEvent( EventName, CiCharacter, 200,

             Options, integer );

Parameters

| EventName (I) | Name of the event to drop. |
| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |

See Also

[sp\_CreateEvent](master_sp_createevent.md)

[sp\_DropAllEvents](master_sp_dropallevents.md)

[sp\_SignalEvent](master_sp_signalevent.md)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.md)

[sp\_WaitForEvent](master_sp_waitforevent.md)

Example

EXECUTE PROCEDURE sp\_DropEvent( my\_event, 0 );
