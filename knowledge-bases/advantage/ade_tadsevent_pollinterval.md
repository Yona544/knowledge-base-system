TAdsEvent.PollInterval




Advantage Database Server 12  

TAdsEvent.PollInterval

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.PollInterval  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.PollInterval Advantage TDataSet Descendant ade\_TAdsEvent.PollInterval Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Properties > TAdsEvent.PollInterval / Dear Support Staff, |  |
| TAdsEvent.PollInterval  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

Used to specify the interval between polls of the shared events table when waiting for the event.

Syntax

property PollInterval: Integer

Description

Only used for local server connections.  The PollInterval is used to specify the interval between polls of the shared events table when waiting for the event.  Zero can be specified to use a default interval (which is currently 300 milliseconds).

See Also

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)