TAdsEvent.EventTimeout




Advantage Database Server 12  

TAdsEvent.EventTimeout

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.EventTimeout  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.EventTimeout Advantage TDataSet Descendant ade\_TAdsEvent.EventTimeout Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Properties > TAdsEvent.EventTimeout / Dear Support Staff, |  |
| TAdsEvent.EventTimeout  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

Maximum time (in milliseconds) to wait for the events to be signaled.

Syntax

property EventTimeout: Integer

Description

The EventTimeout property is used to specify the amount of time to wait for the configured events to be signaled.  Since the TAdsEvent component uses an internal thread to repeatedly wait for the configured events, this property controls the amount of time each execution of the sp\_WaitForAnyEvent canned procedure will wait. Note that the timeout period may not be exact to the millisecond because the call requires a call to the server. The timeout period does not include that turnaround time. A value of -1 can be passed to specify an infinite wait.

See Also

[sp\_WaitForAnyEvent](master_sp_waitforanyevent.htm)