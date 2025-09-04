---
title: Master Sp Waitforevent
slug: master_sp_waitforevent
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_waitforevent.htm
source: Advantage CHM
tags:
  - master
checksum: 38f058d749cf5cbde292b96772c6c58e5d506de3
---

# Master Sp Waitforevent

sp\_WaitForEvent

sp\_WaitForEvent

Advantage SQL Engine

| sp\_WaitForEvent  Advantage SQL Engine |  |  |  |  |

This procedure allows a client to synchronously wait for an event notification to be sent by the server. If an event notification for the specified event has already been sent, then this will return immediately. In other words, the event notification does not have to occur while this procedure is actively waiting. This means that an application can check for an event periodically and use a small (or zero) timeout period.

This procedure will always return immediately when executed by a stored procedure or a trigger or within a script. A client must execute this as a singleton SQL statement in order to actually be able to receive an event notification. If it is executed in a script or by a stored procedure or trigger, the server returns an error.

When a signal is received from an event created with the ADS\_EVENT\_WITH\_DATA option, one record will be returned for each signal that was sent to the event.  The signals will be in the order they were sent and the EventCount of each record will be the signal number rather than the total signal count.  Each record in the result set will also contain the event data from each signal in the StringData field.  Events created without the ADS\_EVENT\_WITH\_DATA option will only return one record when a signal is received, as it has been done in the past.  In that case the EventCount will be the total number of signals that were received by that event and the StringData field will be empty.

Syntax

sp\_WaitForEvent( EventName, char, 200,

                Timeout, integer,

                PollInterval, integer,

                Options, integer );

Timeout, integer,

PollInterval, integer,

Options, integer

);

Parameters

| EventName (I) | Name of the event to wait for. |
| Timeout (I) | Maximum time to wait in milliseconds. 0 means it simply checks to see if a notification message has been sent to the client. It does not actually wait for an event to occur. As long as the client is registered, the server can save the notification to the client even if it is not waiting. Note that the timeout period may not be exact to the millisecond because the call requires a call to the server. The timeout period does not include that turnaround time. A value of -1 can be passed to specify an infinite wait. |
| PollInterval (I) | Only used for local server connections. Remote server connections use an efficient wait mechanism. Used to specify the interval between polls of the shared events table when waiting for the event. Zero can be passed to specify a default interval (which is currently configured at 300 milliseconds). |
| Options (I) | Options, reserved for future use, pass the value 0 for this parameter. |
| EventName (O) | Name of event that was signaled (for completeness and consistency with sp\_WaitForAnyEvent). |
| EventCount (O) | Integer return value that indicates how many times the event was signaled.  A value of 0 means that it timed out (and was not signaled).  If the event was created with the ADS\_EVENT\_WITH\_DATA option, the EventCount is the signal number rather than the total signal count. |
| StringData (O) | Event data that was sent to the event via the sp\_SignalEvent procedure. |

See Also

[sp\_CreateEvent](master_sp_createevent.md)

[sp\_DropAllEvents](master_sp_dropallevents.md)

[sp\_DropEvent](master_sp_dropevent.md)

[sp\_SignalEvent](master_sp_signalevent.md)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.md)

Example

-- wait for up to 2 seconds for the event to be signaled.

EXECUTE PROCEDURE sp\_WaitForEvent( my\_event, 2000, 0, 0 );
