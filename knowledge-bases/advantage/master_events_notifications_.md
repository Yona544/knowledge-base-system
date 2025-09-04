Events (Notifications)




Advantage Database Server 12  

Events (Notifications)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Events (Notifications)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Events (Notifications) Advantage Concepts master\_Events\_notifications\_ Advantage Concepts > Advantage Functionality > Events (Notifications) / Dear Support Staff, |  |
| Events (Notifications)  Advantage Concepts |  |  |  |  |

Event notifications are a mechanism that allows an action at the server to proactively notify clients that an event they are interested in has occurred.

Clients use the canned procedure sp\_CreateEvent to register for event notifications. Once registered, the client can call sp\_WaitForEvent or sp\_WaitForAnyEvent to efficiently wait for the event to be signaled. Events are signaled using the sp\_SignalEvent procedure.

For security purposes, on dictionary-bound connections Advantage will only allow signaling of events from stored procedures or triggers. For example, if you execute the statement "execute procedure sp\_SignalEvent( myevent )" from within ARC or directly in your application, you will get an error.

There is no automatic signaling of events for general updates (must be specifically signaled by user written code in a trigger or stored procedure). In other words, you cannot simply issue an SQL statement that says "wait until someone has updated table X" unless you have written the appropriate trigger to watch for updates.

The signal function sp\_SignalEvent has a parameter that controls whether or not the event is signaled immediately if in a transaction or if it is signaled when the transaction is committed.

Advantage supports many-to-one event delivery. If an event is signaled X times between calls to one of the wait procedures, rather than receiving each signal individually, the wait function returns a count of how many times the event has been signaled since the last wait operation.

If an event is created with the ADS\_EVENT\_WITH\_DATA option, the event can be signaled with a data string which will be returned when the signal is received.  Currently only string data is allowed.  The typical use of this string data is to provide a method of locating the record or table for which a signal is sent, however any string data can be used.  See [sp\_CreateEvent](master_sp_createevent.htm) for more information.  Be aware that event data may be written to disk until it is returned to waiting users and removed from the events subsystem.  The data is stored unencrypted and thus should not contain sensitive information.

Notifications will work with local server, however the efficiency will not be optimal because with no centralized server each client application will be sharing information via a physical "event table" on a file server and will be polling it for changes. The polling interval is configurable and is sent via a parameter to the wait procedures.

Advantage currently only supports synchronous waits for events. This means in most cases the developer will need to create a new thread and a new connection to the database to execute the wait procedures. If the wait procedures are executed on an existing connection, keep in mind that the connection will not be able to process any other database requests until either the event is signaled or it times out. In some situations this may be appropriate, but in other cases you may want an individual thread dedicated to waiting for events.

Note: Multiple local server users connecting to the same data dictionary must use the same connection path in order to share event notifications. Specifically if one user is connecting to the data dictionary on a local drive (e.g. C:\), then they must use the same path as any remote users to share event notifications (e.g. \\server\share). Our recommendation is to use UNC paths for all users.

See Also

[sp\_CreateEvent](master_sp_createevent.htm)

[sp\_DropAllEvents](master_sp_dropallevents.htm)

[sp\_DropEvent](master_sp_dropevent.htm)

[sp\_SignalEvent](master_sp_signalevent.htm)

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)

[sp\_WaitForEvent](master_sp_waitforevent.htm)