Use Semaphore Files




Advantage Database Server 12  

Use Semaphore Files

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Use Semaphore Files  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Use Semaphore Files Advantage Database Server master\_Use\_semaphore\_files Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Use Semaphore Files  Advantage Database Server |  |  |  |  |

Default = 0

Zero indicates that the server will use the [Client Timeout](master_client_timeout.htm) setting will be used to determine if clients have aborted connections rather than the [Semaphore Connection File Path](master_semaphore_connection_file_path.htm) option. Any non-zero value will indicate that the Semaphore Connection File Path configuration parameter should be used. See those sections for more information.

Note For Linux, this parameter is ignored, as semaphore connection files are only used in Advantage for Linux when a 16-bit application connects to the server.