Password




Advantage Database Server 12  

TAdsConnection.Password

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.Password  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.Password Advantage TDataSet Descendant ade\_Password Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.Password  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the password to be used in Advantage Data Dictionary connections.

Syntax

property Password: String;

Description

Provide a value in the Password property when establishing connections to an Advantage Data Dictionary.

Setting the Password property directly is not recommended. As an alternative, use a login dialog and/or the [TAdsConnection.OnLogin](ade_onlogin_tadsconnection.htm) event to control server logins.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[Username](ade_username_tadsconnection.htm)

[LoginPrompt](ade_loginprompt_tadsconnection.htm)

[OnLogin](ade_onlogin_tadsconnection.htm)