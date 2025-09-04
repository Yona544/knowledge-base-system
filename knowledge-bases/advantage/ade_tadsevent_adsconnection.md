TAdsEvent.AdsConnection




Advantage Database Server 12  

TAdsEvent.AdsConnection

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsEvent.AdsConnection  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsEvent.AdsConnection Advantage TDataSet Descendant ade\_TAdsEvent.AdsConnection Advantage TDataSet Descendant > Advantage Components > TAdsEvent > TAdsEvent Properties > TAdsEvent.AdsConnection / Dear Support Staff, |  |
| TAdsEvent.AdsConnection  Advantage TDataSet Descendant |  |  |  |  |

[TAdsEvent](ade_tadsevent.htm)

A reference to the connection this event should clone.

Syntax

property AdsConnection: TAdsConnection;

Description

The AdsConnection property is used to provide the TAdsEvent component with the connection details to be used for Advantage connections.  The TAdsEvent component will instantiate an AdsConnection component for internal use, cloning all appropriate properties from the provided AdsConnection instance.