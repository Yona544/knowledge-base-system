GetTableNames




Advantage Database Server 12  

TAdsConnection.GetTableNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetTableNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetTableNames Advantage TDataSet Descendant ade\_Gettablenames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetTableNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Populates a string list with the tables associated with the connection.

Syntax

procedure TAdsConnection.GetTableNames( poList : TStrings; strFileMask : String );

Description

Use GetTableNames to get a list of tables associated with the TAdsConnection component. The [TAdsConnection.IsConnected](ade_isconnected_tadsconnection.htm) property must be set to True before calling GetTableNames. If GetTableNames is called on a connection that uses the [TAdsConnection.ConnectPath](ade_connectpath_tadsconnection.htm) property, all files matching the strFileMask parameter will be returned. If GetTableNames is called on a connection that uses the [TAdsConnection.AliasName](ade_aliasname_tadsconnection.htm) property, tables matching the alias tabletype will be returned, and the strMask parameter will be ignored. If GetTableNames is called using an alias that points to an Advantage Data Dictionary, or a connection path that points to an Advantage Data Dictionary, the strFileMask parameter will be ignored, and all tables registered in the data dictionary will be returned.

See Also

[AliasName](ade_aliasname_tadsconnection.htm)

[ConnectPath](ade_connectpath_tadsconnection.htm)