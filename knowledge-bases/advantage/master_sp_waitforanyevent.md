sp\_WaitForAnyEvent




Advantage Database Server 12  

sp\_WaitForAnyEvent

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_WaitForAnyEvent  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_WaitForAnyEvent Advantage SQL Engine master\_Sp\_waitforanyevent Advantage SQL > System Procedures > Procedures > sp\_WaitForAnyEvent / Dear Support Staff, |  |
| sp\_WaitForAnyEvent  Advantage SQL Engine |  |  |  |  |

This procedure allows a connection to wait for an event notification for any event that it has created. If an event notification for any event has already been signaled, then this will return immediately. In other words, the event notification does not have to occur while this procedure is actively waiting. This means that an application can check for events periodically and use a small (or zero) timeout period.

If multiple events have been signaled, then the actual event that gets returned is nondeterministic.

When a signal is received from an event created with the ADS\_EVENT\_WITH\_DATA option, one record will be returned for each signal that was sent to the event.  The signals will be in the order they were sent and the EventCount of each record will be the signal number rather than the total signal count.  Each record in the result set will also contain the event data from each signal in the StringData field.  Events created without the ADS\_EVENT\_WITH\_DATA option will only return one record when a signal is received, as it has been done in the past.  In that case the EventCount will be the total number of signals that were received by that event and the StringData field will be empty.

This procedure will always return immediately when executed by a stored procedure or a trigger or within a script. A client must execute this as a singleton SQL statement in order to actually be able to receive an event notification. If it is executed in a script or by a stored procedure or trigger, an error will be returned.

Syntax

sp\_WaitForAnyEvent( Timeout, integer,

                   PollInterval, integer,

                   Options, integer);

 

Parameters

|  |  |
| --- | --- |
| Timeout (I) | Maximum time to wait in milliseconds. 0 means it simply checks to see if a notification message has been sent to the client. It does not actually wait for an event to occur. As long as the client is registered, the server can save the notification to the client even if it is not waiting. Note that the timeout period may not be exact to the millisecond because the call requires a call to the server. The timeout period does not include that turnaround time. A value of -1 can be passed to specify an infinite wait. |
| PollInterval (I) | Only used for local server connections. Remote server connections use an efficient wait mechanism. Used to specify the interval between polls of the shared events table when waiting for the event. Zero can be passed to specify a default interval (which is currently configured at 300 milliseconds). |
| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |
| EventName (O) | Name of event that was signaled. |
| EventCount (O) | Integer return value that indicates how many times the event was signaled.  A value of 0 means that it timed out (and was not signaled).  If the event was created with the ADS\_EVENT\_WITH\_DATA option, the EventCount is the signal number rather than the total signal count. |
| StringData (O) | Event data that was sent to the event via the sp\_SignalEvent procedure. |

See Also

[sp\_CreateEvent](master_sp_createevent.htm)

[sp\_DropAllEvents](master_sp_dropallevents.htm)

[sp\_DropEvent](master_sp_dropevent.htm)

[sp\_SignalEvent](master_sp_signalevent.htm)

[sp\_WaitForEvent](master_sp_waitforevent.htm)

Example

-- wait for up to 2 seconds for any event to be signaled.

EXECUTE PROCEDURE sp\_WaitForAnyEvent( 2000, 0, 0 );