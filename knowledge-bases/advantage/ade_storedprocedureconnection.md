StoredProcedureConnection




Advantage Database Server 12  

TAdsConnection.StoredProcedureConnection

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.StoredProcedureConnection  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.StoredProcedureConnection Advantage TDataSet Descendant ade\_Storedprocedureconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.StoredProcedureConnection  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies if this connection lives within a stored procedure executed on the behalf of remote clients.

Syntax

property StoredProcedureConnection: Boolean;

Description

Set StoredProcedureConnection to True when writing a stored procedure. If this property is set to True the application will not increment the server user count for the stored procedure. If this option is not set, then the stored procedure will increment the server user count, which will prevent other users from connecting when the user count reaches the maximum.

Note If this option is not set, all connections from all stored procedures will increase the user count by at most one user.

The StoredProcedureConnection property only affects connections to the [Advantage Database Server](master_advantage_database_server.htm). Connections to [Advantage Local Server](master_advantage_local_server.htm) are not affected by this property.

Example

procedure TMyStoredProc.OpenFiles (Sender: TObject);

 

begin

 

{\* Set flag because this is a stored procedure object \*}

AdsConnection.StoredProcedureConnection := TRUE;

 

{\* Open the table for the entire stored procedure session \*}

DemoTable.Open;

 

end;