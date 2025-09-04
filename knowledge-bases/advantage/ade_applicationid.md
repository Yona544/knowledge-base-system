ApplicationID




Advantage Database Server 12  

TAdsConnection.ApplicationID

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.ApplicationID  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.ApplicationID Advantage TDataSet Descendant ade\_Applicationid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.ApplicationID  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the Application ID for the connection. If this property is left empty, the Application ID is initialized to be the file name of the application (executable) that created the connection.

For efficiency, this property is only used to specify the ApplicationID, it is not automatically populated on connection. To read the ApplicationID of an active connection, call the TAdsConnection.GetApplicationID method.

This property is not used internally by Advantage, but provided strictly for use by application developers. The ApplicationID is often used for auditing purposes.

The ApplicationID is a wrapper around the canned procedures sp\_SetApplicationID and sp\_GetApplicationID.

Syntax

property ApplicationID: String;

Description

Provide a value in the ApplicationID property.

See Also

[TAdsConnection.GetApplicationID](ade_getapplicationid.htm)