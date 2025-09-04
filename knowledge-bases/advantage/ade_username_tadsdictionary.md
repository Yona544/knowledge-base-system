Username




Advantage Database Server 12  

TAdsDictionary.Username

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.Username  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.Username Advantage TDataSet Descendant ade\_Username\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.Username  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Specifies the username to be used in Advantage Data Dictionary connections.

Syntax

property Username: String;

Description

Provide a value in the Username property when establishing connections to an Advantage Data Dictionary.

The Username property is also used to initialize the default login dialog if using [TAdsDictionary.LoginPrompt](ade_loginprompt__tadsdictionary.htm). After a successful Data Dictionary login, the user name used during the login is stored in the Username property.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.