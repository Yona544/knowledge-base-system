BeforeCommit




Advantage Database Server 12  

TAdsConnection.BeforeCommit

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.BeforeCommit  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.BeforeCommit Advantage TDataSet Descendant ade\_Beforecommit Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.BeforeCommit  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

BeforeCommit occurs before an application makes a request to commit modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property BeforeCommit: TNotifyEvent;

Description

Write a BeforeCommit event handler to take specific action before an application commits changes to the current transaction.