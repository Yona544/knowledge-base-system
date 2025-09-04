sp\_DropEvent




Advantage Database Server 12  

sp\_DropEvent

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropEvent  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropEvent Advantage SQL Engine master\_Sp\_dropevent Advantage SQL > System Procedures > Procedures > sp\_DropEvent / Dear Support Staff, |  |
| sp\_DropEvent  Advantage SQL Engine |  |  |  |  |

This procedure removes the event for the active connection.

Syntax

sp\_DropEvent( EventName, CiCharacter, 200,

             Options, integer );

Parameters

|  |  |
| --- | --- |
| EventName (I) | Name of the event to drop. |
| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |

See Also

[sp\_CreateEvent](master_sp_createevent.htm)

[sp\_DropAllEvents](master_sp_dropallevents.htm)

[sp\_SignalEvent](master_sp_signalevent.htm)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)

[sp\_WaitForEvent](master_sp_waitforevent.htm)

Example

EXECUTE PROCEDURE sp\_DropEvent( my\_event, 0 );