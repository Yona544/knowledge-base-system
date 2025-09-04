Suppress Message Boxes




Advantage Database Server 12  

Suppress Message Boxes

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Suppress Message Boxes  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Suppress Message Boxes Advantage Database Server master\_Suppress\_message\_boxes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Suppress Message Boxes  Advantage Database Server |  |  |  |  |

Default = 0

If the SUPPRESS\_MESSAGE\_BOXES configuration parameter is set to a non-zero value, then the Advantage Database Server will not display error message boxes caused by startup errors, exceptions, or shutdown errors. For example, when a request is made to shut down Advantage Database Server while it has active connections, it will, by default, prompt with a Yes/No message box asking if that is desired. If this configuration parameter has a non-zero value, then the server will log an entry to the application event log and silently shut down. This may be useful in a clustered environment where the cluster manager is responsible for starting and stopping Advantage Database Server automatically without human interaction.

Note This parameter is only applicable to Advantage Database Server for Windows.