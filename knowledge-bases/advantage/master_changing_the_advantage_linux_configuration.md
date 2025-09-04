Changing the Advantage Linux Configuration




Advantage Database Server 12  

Changing the Advantage Linux Configuration

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Changing the Advantage Linux Configuration  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Changing the Advantage Linux Configuration Advantage Database Server master\_Changing\_the\_advantage\_linux\_configuration Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Changing the Advantage Linux Configuration  Advantage Database Server |  |  |  |  |

To change the Advantage Linux configuration via the command line, you must kill the Advantage daemon then restart it with new configuration parameters.

Example:

./adsd -C50 -W75 -D100 &