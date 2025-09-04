Username




Advantage Database Server 12  

TAdsConnection.Username

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.Username  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.Username Advantage TDataSet Descendant ade\_Username\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.Username  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the username to be used in Advantage Data Dictionary connections.

Syntax

property Username: String;

Description

Provide a value in the Username property when establishing connections to an Advantage Data Dictionary.

The Username property is also used to initialize the default login dialog if using [TAdsConnection.LoginPrompt](ade_loginprompt_tadsconnection.htm). After a successful Data Dictionary login, the user name used during the login is stored in the Username property.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[Password](ade_password.htm)

[LoginPrompt](ade_loginprompt_tadsconnection.htm)

[OnLogin](ade_onlogin_tadsconnection.htm)