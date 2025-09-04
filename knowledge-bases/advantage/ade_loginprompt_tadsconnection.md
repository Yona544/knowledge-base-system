LoginPrompt




Advantage Database Server 12  

TAdsConnection.LoginPrompt

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.LoginPrompt  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.LoginPrompt Advantage TDataSet Descendant ade\_Loginprompt\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.LoginPrompt  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies whether a login dialog appears immediately before opening a new connection.

Syntax

property LoginPrompt: Boolean;

Description

The LoginPrompt property is only used if connecting to an Advantage Data Dictionary.

If LoginPrompt is set to True, a dialog appears to prompt users for a username and password. The current username is read from the TAdsConnection.Username property, and a standard Login dialog box opens. The dialog prompts for a user name and password combination, and then uses the values entered by the user to attempt a connection.

The OnLogin event is only fired when the LoginPrompt value is True, and can be used to bypass the default login dialog and provide your own dialog or other login method that returns a username and password to be used to establish the connection.

If LoginPrompt is set to False the application must provide a username and password programmatically. Set the TAdsConnection.Username and TAdsConnection.Password properties prior to setting [TAdsConnection.IsConnected](ade_isconnected_tadsconnection.htm) to True.

Delphi 6 or greater Users: If using the default login dialog, you must add the DBLogDlg (or QDBLogDlg if using CLX) unit to the uses clause of the unit that declares the connection component. See the Delphi "Controlling Server Login" documentation for more details.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.

See Also

[OnLogin](ade_onlogin_tadsconnection.htm)

[Username](ade_username_tadsconnection.htm)

[Password](ade_password.htm)