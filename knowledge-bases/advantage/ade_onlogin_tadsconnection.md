OnLogin




Advantage Database Server 12  

TAdsConnection.OnLogin

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.OnLogin  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.OnLogin Advantage TDataSet Descendant ade\_Onlogin\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.OnLogin  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

OnLogin occurs when an application connects to a database.

Syntax

type TAdsDatabaseLoginEvent = procedure( AdsConnection: TAdsConnection;

var Username : String;

var Password : String ) of object;

 

property OnLogin: TAdsDatabaseLoginEvent;

Description

Write an OnLogin event handler to take specific actions when an application attempts to connect to a database. Values returned in the Username and Password parameters are passed to the Advantage Database Server in the connection attempt.

The OnLogin event is only fired if the [TAdsConnection.LoginPrompt](ade_loginprompt_tadsconnection.htm) property is set to True.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[LoginPrompt](ade_loginprompt_tadsconnection.htm)

[Username](ade_username_tadsconnection.htm)

[Password](ade_password.htm)