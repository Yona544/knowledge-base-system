TAdsEvent.OnLog




Advantage Database Server 12  

TAdsEvent.OnLog

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.OnLog  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.OnLog Advantage TDataSet Descendant ade\_TAdsEvent.OnLog Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Events > TAdsEvent.OnLog / Dear Support Staff, |  |
| TAdsEvent.OnLog  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

OnLog occurs when debug information is available.

Syntax

type TAdsLogEvent = procedure ( Sender : TObject;

                               log : String ) of object;

property OnLog : TAdsLogEvent;

Description

Write an OnLog event handler to receive debug information about internal activities and any exceptions that may occur in the TAdsEvent component.

This event is called using the TThread.Synchronize method, which means the main Delphi VCL thread will not be able to interact with the user interface while executing this event. The OnLog event handler should be kept short and efficient.