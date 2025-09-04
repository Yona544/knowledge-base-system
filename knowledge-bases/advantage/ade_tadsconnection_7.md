TAdsConnection




Advantage Database Server 12  

TAdsConnection

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection Advantage TDataSet Descendant ade\_Tadsconnection\_7 Advantage TDataSet Descendant > Advantage Components > TAdsConnection / Dear Support Staff, |  |
| TAdsConnection  Advantage TDataSet Descendant |  |  |  |  |

|  |  |  |
| --- | --- | --- |
| [Properties](ade_tadsconnection_properties.htm) | [Methods](ade_tadsconnection_methods.htm) | [Events](ade_tadsconnection_events.htm) |

 

TAdsConnection is a component that is similar to the Delphi TDatabase component. TAdsConnection defines a connection to the Advantage Database Server.

Unit

AdsCnnct

Description

The TAdsConnection component is similar to the Delphi TDatabase component. TAdsConnection is used primarily for connection management and performing connection-specific functionality such as transaction processing.

To use the TAdsConnection component, create a new instance by placing a TAdsConnection component on a form, data module, or by instantiating and instance in code. Then, modify every TAdsTable and TAdsQuery component to be associated with this connection by setting its AdsConnection property to reference this new TAdsConnection component.

You may create multiple TAdsConnection components to force multiple server connections. This is valuable when you want to connect to two different servers within your application or if you need to have some tables/cursors open via one Advantage server type and others open via a different Advantage server type. Using one TAdsConnection component per thread also allows for the highest level of concurrency in a multi-threaded Advantage application.

When the TAdsConnection.BeginTransaction method is called, every TAdsTable associated with the connection component will enter the transaction. Since more than one connection component may be used, multiple independent transactions can be processed concurrently.

Advantage Database Server licensing is based on concurrent users, not concurrent connections. Therefore, using two connection components to the same server only uses one license.

Delphi 6 or greater If using the default login dialog, you must add the DBLogDlg (or QDBLogDlg if using CLX) unit to the uses clause of the unit that declares the connection component. See the Delphi "Controlling Server Login" documentation for more details.