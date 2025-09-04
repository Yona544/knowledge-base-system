CreateFromHandle




Advantage Database Server 12  

TAdsConnection.CreateFromHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.CreateFromHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.CreateFromHandle Advantage TDataSet Descendant ade\_CreateFromHandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.CreateFromHandle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Creates a new TAdsConnection component, using an active Advantage Client Engine (ACE) handle.

Syntax

constructor CreateFromHandle(Owner: TComponent; Handle : ADSHANDLE; strName : string );

Description

Used to setup an active TAdsConnection instance from an existing ACE handle, but unlike [CreateWithHandle](ade_createwithhandle.htm) which takes on the ACE connection handle, this method will get its own new ACE connection, which will be based on the values it takes from the existing connection.

If the handle passed in is a database connection, the username and password properties of the TAdsConnection instance will be populated.

 

See Also

[CreateWithHandle](ade_createwithhandle.htm)