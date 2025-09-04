Password




Advantage Database Server 12  

TAdsDictionary.Password

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.Password  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.Password Advantage TDataSet Descendant ade\_Password\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.Password  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Specifies the password to be used in Advantage Data Dictionary connections.

Syntax

property Password: String;

Description

Provide a value in the Password property when establishing connections to an Advantage Data Dictionary.

Setting the Password property directly is not recommended. As an alternative, use a login dialog and/or the TAdsDictionary.OnLogin event to control server logins.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.