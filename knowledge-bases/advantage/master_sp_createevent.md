sp\_CreateEvent




Advantage Database Server 12  

sp\_CreateEvent

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_CreateEvent  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_CreateEvent Advantage SQL Engine master\_Sp\_createevent Advantage SQL > System Procedures > Procedures > sp\_CreateEvent / Dear Support Staff, |  |
| sp\_CreateEvent  Advantage SQL Engine |  |  |  |  |

This procedure allows a client to create an event of the given name. Once it has created the event, a client will start receiving notifications whenever that event is signaled whether or not the client is actively waiting for the event or not. If the client is not actively waiting, the event will be saved by the server until the client application waits for the event.

If the ADS\_EVENT\_WITH\_DATA (2) option is set, the event will accept string data of any size.  A user must create the event with the data option in order to receive event data from a signal.  Events created without the data option will not return event data even if the signal provided event data.

Each connection that is interested in a specific event must call sp\_CreateEvent. When an event of a given name is signaled, the event notification will be sent to all connections that have called sp\_CreateEvent for that event name.

Note: Multiple local server users connecting to the same data dictionary must use the same connection path in order to share event notifications. Specifically if one user is connecting to the data dictionary on a local drive (e.g. C:\), then they must use the same path as any remote users to share event notifications (e.g. \\server\share). Our recommendation is to use UNC paths for all users.

Syntax

sp\_CreateEvent( EventName, CiCharacter, 200,

               Options, integer );

 

Parameters

|  |  |
| --- | --- |
| EventName (I) | Name of the event to register. |
| Options (I) | Options. Pass 0 for default behavior. Pass 2 to create an event that will receive event data from a signal. |

See Also

[sp\_DropAllEvents](master_sp_dropallevents.htm)

[sp\_DropEvent](master_sp_dropevent.htm)

[sp\_SignalEvent](master_sp_signalevent.htm)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)

[sp\_WaitForEvent](master_sp_waitforevent.htm)

Example

// NOTE: This example requires a data dictionary connection

// Create an event that accepts data

EXECUTE PROCEDURE sp\_CreateEvent( 'my\_event', 2 /\* ADS\_EVENT\_WITH\_DATA \*/ );  
   
// Create a simple test table  
CREATE TABLE my\_table ( name char (10));  
   
// Create a trigger that signals the event and includes the ROWID of the updated record  
CREATE TRIGGER my\_trig ON my\_table AFTER INSERT  
BEGIN  
   EXECUTE PROCEDURE sp\_SignalEvent( 'my\_event', false, 0, ::stmt.TrigRowID );   
END;  
   
// A simple INSERT will fire the trigger and signal the event  
INSERT INTO my\_table VALUES ( 'Charles' );  
   
// Now when we get the signal we can use the ROWID to find the updated record  
SELECT \* FROM my\_Table WHERE ROWID = ( SELECT StringData FROM ( EXECUTE PROCEDURE sp\_WaitForEvent( 'my\_event', 0, 0, 0 )) Sig );