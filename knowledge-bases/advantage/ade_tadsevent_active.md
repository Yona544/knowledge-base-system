TAdsEvent.Active




Advantage Database Server 12  

TAdsEvent.Active

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.Active  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.Active Advantage TDataSet Descendant ade\_TAdsEvent.Active Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Properties > TAdsEvent.Active / Dear Support Staff, |  |
| TAdsEvent.Active  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

Defines whether the event listener is active.

Syntax

property Active: Boolean;

Description

When the true, the listener will wait for the associated event(s) to be signaled.

When set to false, TAdsEvent will terminate its background thread that is waiting on events. This thread termination is synchronous and can take up to 2 seconds, depending on the [EventTimeout](ade_tadsevent_eventtimeout.htm) property setting. If the EventTimeout setting is -1, or over 2000, it can take 2 full seconds to terminate the thread. If EventTimeout is less than 2000, the thread can be terminated in the same number of milliseconds as EventTimeout specifies. When using the Advantage Local Server the thread can be terminated in the same number of milliseconds as the [PollInterval](ade_tadsevent_pollinterval.htm) property specifies.