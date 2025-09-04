Semaphore Connection File Path Info




Advantage Database Server 12  

Semaphore Connection File Path Info

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Semaphore Connection File Path Info |  |  | Feedback on: Advantage Database Server 12 - Semaphore Connection File Path Info arc\_Semaphore\_connection\_file\_path\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Semaphore Connection File Path Info |  |  |  |  |

When an Advantage application connects to the Advantage Database Server, it establishes a connection between the workstation and the Advantage Database Server. A semaphore connection file is opened to aid in determining the connection status between the workstation and the Advantage Database Server service. The default directory in which this semaphore connection file is opened is the server directory where the first database file is to be opened.

Note Semaphore connection files are only used if the configuration parameter Use\_Semaphore\_Files is set to a non-zero value. The default is zero to indicate that semaphore connection files are not used at all. See the configuration option Use\_Semaphore\_Files in the Advantage Database Server Help documentation (ADS.HLP) for more information.