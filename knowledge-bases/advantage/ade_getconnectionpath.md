GetConnectionPath




Advantage Database Server 12  

TAdsConnection.GetConnectionPath

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetConnectionPath  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetConnectionPath Advantage TDataSet Descendant ade\_Getconnectionpath Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetConnectionPath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Returns the connection path from the TAdsConnection component.

Syntax

function GetConnectionPath : string;

Remarks

This function returns the connection path from the TAdsConnection component. If the connection is using an alias, the connection path associated with the alias will be returned. If the connection is to a data dictionary, this path will NOT contain the name of the data dictionary file (see [GetConnectionWithDDPath](ade_getconnectionwithddpath.htm)).

See Also

[GetConnectionWithDDPath](ade_getconnectionwithddpath.htm)

[AliasName](ade_aliasname_tadsconnection.htm)

[ConnectPath](ade_connectpath_tadsconnection.htm)