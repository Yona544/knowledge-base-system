sp\_DropAllEvents




Advantage Database Server 12  

sp\_DropAllEvents

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropAllEvents  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropAllEvents Advantage SQL Engine master\_Sp\_dropallevents Advantage SQL > System Procedures > Procedures > sp\_DropAllEvents / Dear Support Staff, |  |
| sp\_DropAllEvents  Advantage SQL Engine |  |  |  |  |

This procedure removes all events for the connection.

Syntax

sp\_DropAllEvents( Options, integer );

Parameters

|  |  |
| --- | --- |
| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |

See Also

[sp\_CreateEvent](master_sp_createevent.htm)

[sp\_DropEvent](master_sp_dropevent.htm)

[sp\_SignalEvent](master_sp_signalevent.htm)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)

[sp\_WaitForEvent](master_sp_waitforevent.htm)

Example

EXECUTE PROCEDURE sp\_DropAllEvents( 0 );