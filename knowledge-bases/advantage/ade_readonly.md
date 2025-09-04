ReadOnly




Advantage Database Server 12  

TAdsConnection.ReadOnly

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.ReadOnly  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.ReadOnly Advantage TDataSet Descendant ade\_Readonly Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.ReadOnly  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies that the connection provides read-only access.

Syntax

property ReadOnly : Boolean read FReadOnly write FReadOnly;

Description

Use the ReadOnly property to specify if a connection should allow datasets attached to it to modify data. If this property is set to True, all datasets opened on the connection will open tables in readonly mode, regardless of the individual datasets ReadOnly property setting.

This property is helpful when distributing an application that will open a database that is stored on read-only media, such as a CD-ROM. Note that this setting does not affect UPDATE, INSERT, and DELETE statements. Those statements can still be executed on query instances associated with this connection.