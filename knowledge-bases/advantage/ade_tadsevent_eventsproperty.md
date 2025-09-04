TAdsEvent.EventsProperty




Advantage Database Server 12  

TAdsEvent.Events

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.Events  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.Events Advantage TDataSet Descendant ade\_TAdsEvent.EventsProperty Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Properties > TAdsEvent.Events / Dear Support Staff, |  |
| TAdsEvent.Events  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

A case insensitive list of the events this component should listen to.

Syntax

property Events: TStrings

Description

The Events property is used to define a case-insensitive list of event names for which the component should wait.  The component will create each event via the sp\_CreateEvent stored procedure, then wait for each of the events to be signaled.