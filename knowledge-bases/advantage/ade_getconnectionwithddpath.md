GetConnectionWithDDPath




Advantage Database Server 12  

TAdsConnection.GetConnectionWithDDPath

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetConnectionWithDDPath  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetConnectionWithDDPath Advantage TDataSet Descendant ade\_Getconnectionwithddpath Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetConnectionWithDDPath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Returns the connection path from the TAdsConnection component.

Syntax

function GetConnectionWithDDPath : string;

Remarks

This function returns the connection path from the TAdsConnection component. If the connection is to a data dictionary, this path will contain the name of the data dictionary file. If the connection does not reference a data dictionary, this function behaves the same as [GetConnectionPath](ade_getconnectionpath.htm).

See Also

[GetConnectionPath](ade_getconnectionpath.htm)

[AliasName](ade_aliasname_tadsconnection.htm)

[ConnectPath](ade_connectpath_tadsconnection.htm)