AfterCommit




Advantage Database Server 12  

TAdsConnection.AfterCommit

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.AfterCommit  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.AfterCommit Advantage TDataSet Descendant ade\_Aftercommit Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.AfterCommit  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

AfterCommit occurs after an application completes a request to commit modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property AfterCommit: TNotifyEvent;

Description

Write an AfterCommit event handler to take specific action after an application commits changes to the current transaction.