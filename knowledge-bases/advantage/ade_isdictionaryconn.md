IsDictionaryConn




Advantage Database Server 12  

TAdsConnection.IsDictionaryConn

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.IsDictionaryConn  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.IsDictionaryConn Advantage TDataSet Descendant ade\_Isdictionaryconn Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.IsDictionaryConn  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies if the connection is to an Advantage Data Dictionary.

Syntax

property IsDictionaryConn: Boolean;

Description

IsDictionaryConn can be retrieved after the IsConnected property is set to TRUE to determine whether the connection is an Advantage Data Dictionary connection, or a standard Advantage connection.

Note You are not required to check if a connection is to an Advantage Data Dictionary, this property is only provided as an information property you may find useful when updating existing applications that may want to change their behavior depending on the connection type. If you specify a dictionary alias or connection path (for example, x:\mydata\mydictionary.add) and that file can not be opened an error will be returned, you do NOT have to inspect IsDictionaryConn to determine if the application opened the dictionary.