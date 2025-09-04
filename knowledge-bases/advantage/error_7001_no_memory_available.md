7001 No memory available




Advantage Database Server 12  

7001 No memory available

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7001 No memory available  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7001 No memory available Advantage Error Guide error\_7001\_no\_memory\_available Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7001 No memory available  Advantage Error Guide |  |  |  |  |

Problem: If connected to the Advantage Database Server, there is not enough available free RAM on the server. If connected to the Advantage Local Server, there is not enough available free RAM on the client.

Solution: If using the Advantage Database Server, lower Advantage Database Server configurable settings (via the Advantage Configuration Utility for the Advantage Database Server for Windows or ADS.CONF for the Advantage Database Server for Linux) so that less memory is required or add RAM to the server. Then re-load/re-start the Advantage Database Server. If using the Advantage Local Server, lower Advantage Local Server configurable settings via ADSLOCAL.CFG so that less memory is required or add RAM to the client. Then re-start the application using the Advantage Local Server.