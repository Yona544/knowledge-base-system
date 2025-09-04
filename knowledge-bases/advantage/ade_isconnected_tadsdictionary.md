IsConnected




Advantage Database Server 12  

TAdsDictionary.IsConnected

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.IsConnected  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.IsConnected Advantage TDataSet Descendant ade\_Isconnected\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.IsConnected  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Specifies whether or not the connection has been established.

Syntax

property IsConnected: Boolean;

Description

Use IsConnected to determine or set a connection. If the setting IsConnected to True:

|  |  |
| --- | --- |
| · | Triggers the OnConnect event handler if one is defined for the data dictionary component. |

|  |  |
| --- | --- |
| · | Opens a connection to the server. |

If an error occurs during the getting of the connection, IsConnected is set to False.