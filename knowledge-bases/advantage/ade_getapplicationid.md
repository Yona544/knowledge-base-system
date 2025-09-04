GetApplicationID




Advantage Database Server 12  

TAdsConnection.GetApplicationID

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetApplicationID  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetApplicationID Advantage TDataSet Descendant ade\_Getapplicationid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetApplicationID  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Retrieves the Application ID from the server.

Syntax

function GetApplicationID : String;

Description

GetApplicationID returns the ApplicationID as a string from the current connection in the server.

Note: If GetApplicationID was used when it is not connected to the server, then GetApplicationID method will just return whatever value in the property, not in the server.

Example

procedure TForm1.Test();

var

appID : String;

begin

{\* Get the ApplicationID \*}

appID := AdsConnection1.GetApplicationID();

end;

See Also

[TAdsConnection.ApplicationID](ade_applicationid.htm)