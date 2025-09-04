TAdsEvent.OnNotification




Advantage Database Server 12  

TAdsEvent.OnNotification

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.OnNotification  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.OnNotification Advantage TDataSet Descendant ade\_TAdsEvent.OnNotification Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Events > TAdsEvent.OnNotification / Dear Support Staff, |  |
| TAdsEvent.OnNotification  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

OnNotification occurs when any configured event is signalled.

Syntax

type TAdsNotifyEvent = procedure ( Sender : TObject;

                                  event : String;

                                  count : Integer;

                                  eventdata : String ) of object;   
property OnNotification : TAdsNotifyEvent;

Parameters

Sender:  Object reference of the event sender

Event : Name of the event that was signaled

Count : Number of times the event has been signaled

EventData : Any data returned by the event signal

 

Description

Write an OnNotification event handler to take appropriate actions within your application when a configured notification is signaled.

This event is called using the TThread.Synchronize method, which means the main Delphi VCL thread will not be able to interact with the user interface while executing this event. The OnLog event handler should be kept short and efficient.