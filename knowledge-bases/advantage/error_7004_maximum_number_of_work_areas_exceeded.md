7004 Maximum number of work areas exceeded




Advantage Database Server 12  

7004 Maximum number of work areas exceeded

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7004 Maximum number of work areas exceeded  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7004 Maximum number of work areas exceeded Advantage Error Guide error\_7004\_maximum\_number\_of\_work\_areas\_exceeded Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7004 Maximum number of work areas exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The maximum number of configured work areas are already in use and the Advantage server was unable to allocate more resources for additional work areas.

Solution: Increase the setting for the "Number of Work Areas" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the WORKAREAS configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

Advantage Local Server

Problem: The maximum number of configured work areas are already in use and the Advantage server was unable to allocate more resources for additional work areas.

Solution: Increase the setting for the WORKAREAS configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. If no WORKAREAS configuration key exists in ADSLOCAL.CFG, add one and set the value to larger than the number of CONNECTIONS multiplied by 25 (which is the default value for the number of work areas if no WORKAREAS configuration key exists). Then re-start the application that uses the Advantage Local Server.