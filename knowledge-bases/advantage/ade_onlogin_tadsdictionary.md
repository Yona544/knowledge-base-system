OnLogin




Advantage Database Server 12  

TAdsDictionary.OnLogin

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.OnLogin  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.OnLogin Advantage TDataSet Descendant ade\_Onlogin\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.OnLogin  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

OnLogin occurs when an application connects to a database.

Syntax

type TAdsDatabaseLoginEvent = procedure( AdsConnection: TAdsConnection;

var Username : String;

var Password : String ) of object;

 

property OnLogin: TAdsDatabaseLoginEvent;

Description

Write an OnLogin event handler to take specific actions when an application attempts to connect to a database. Values returned in the Username and Password parameters are passed to the Advantage Database Server in the connection attempt.

The OnLogin event is only fired if the [TAdsDictionary.LoginPrompt](ade_loginprompt__tadsdictionary.htm) property is set to True.

Note Storing hard-coded user name and password entries as property values or in code for an OnLogin event handler can compromise server security.