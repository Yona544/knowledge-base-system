sp\_SignalEvent




Advantage Database Server 12  

sp\_SignalEvent

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_SignalEvent  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_SignalEvent Advantage SQL Engine master\_Sp\_signalevent Advantage SQL > System Procedures > Procedures > sp\_SignalEvent / Dear Support Staff, |  |
| sp\_SignalEvent  Advantage SQL Engine |  |  |  |  |

This procedure provides the mechanism by which an application can cause an event notification to be signaled. For security reasons, on dictionary-bound connections sp\_SignalEvent can only be called by a trigger or a stored procedure. If you want to be able to signal an event from a client with a simple SQL statement execution, you can create your own stored procedure that wraps this system procedure.

The EventData parameter is used to pass event data to the event.  Typically the event data is used to give the recipient of the signal enough information to locate the table or record that was updated.  The primary key or ROWID value from the updated table are good values to use to locate the updated record.  Any string data can be sent to the event, Advantage simply passes it through the events subsystem.  Note that only events that are created with the ADS\_EVENT\_WITH\_DATA option can receive event data from a signal.  See [sp\_CreateEvent](master_sp_createevent.htm) for more information.

Syntax

sp\_SignalEvent( EventName, char, 200,

               WaitForCommit, logical,

               Options, integer );

 

sp\_SignalEvent( EventName, char, 200,

               WaitForCommit, logical,

               Options, integer,

               EventData, memo

               );

WaitForCommit, logical,

Options, integer

);

Parameters

|  |  |
| --- | --- |
| EventName (I) | Name of the event to signal |
| WaitForCommit (I) | This indicates if the event is to be signaled at commit time if a transaction is active. If a transaction is active and this flag is true, then the event notification will be sent only when the transaction is committed. If the transaction is rolled back, the event will not be signaled. If there is no active transaction or this flag is false, then the event notification will occur immediately. |
| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |
| EventData (I) | Optional string value to pass to the event. |

See Also

[sp\_CreateEvent](master_sp_createevent.htm)

[sp\_DropAllEvents](master_sp_dropallevents.htm)

[sp\_DropEvent](master_sp_dropevent.htm)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)

[sp\_WaitForEvent](master_sp_waitforevent.htm)

Example

CREATE TRIGGER [UpdateCustomer]

ON CUSTOMER

AFTER UPDATE

BEGIN

EXECUTE PROCEDURE sp\_SignalEvent( my\_event, false, 0 );

END;

Example

CREATE TRIGGER [UpdateCustomer]

ON CUSTOMER

AFTER UPDATE

BEGIN  

  // Pass the ROWID from the updated table to the event

  EXECUTE PROCEDURE sp\_SignalEvent( my\_event, false, 0, ::stmt.TrigRowID );

END;