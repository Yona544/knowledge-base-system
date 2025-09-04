7007 Maximum number of locks exceeded




Advantage Database Server 12  

7007 Maximum number of locks exceeded

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7007 Maximum number of locks exceeded  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7007 Maximum number of locks exceeded Advantage Error Guide error\_7007\_maximum\_number\_of\_locks\_exceeded Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7007 Maximum number of locks exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The maximum number of configured locks are already in use and the Advantage server was unable to allocate more resources for additional locks.

Solution: Increase the setting for the "Number of Data Locks" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the LOCKS configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

Advantage Local Server

Problem: The maximum number of configured locks are already in use and the Advantage server was unable to allocate more resources for additional locks.

Solution: Increase the setting for the LOCKS configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. Then re-start the application that uses the Advantage Local Server.