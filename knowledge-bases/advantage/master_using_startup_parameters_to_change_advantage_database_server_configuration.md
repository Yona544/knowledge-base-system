Using Startup Parameters to Change Advantage Database Server Configuration




Advantage Database Server 12  

Using Startup Parameters to Change Advantage Database Server Configuration

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Startup Parameters to Change Advantage Database Server Configuration  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Using Startup Parameters to Change Advantage Database Server Configuration Advantage Database Server master\_Using\_startup\_parameters\_to\_change\_advantage\_database\_server\_configuration Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Using Startup Parameters to Change Advantage Database Server Configuration  Advantage Database Server |  |  |  |  |

To change the Advantage Database Server Service configuration using Startup Parameters, you must stop the Advantage Database Server Service and re-start it with new configuration parameters specified in the "Startup Parameters" box (with Windows NT 4.0) or "Start parameters" edit box (with Windows 2000/2003) located in the Service Control Manager.

Enter the desired configuration changes into the "Startup Parameters" box (with Windows NT 4.0) or "Start parameters" edit box (with Windows 2000/2003). For example, if you wish to change the Advantage Database Server service configuration to 15 connections, 125 work areas and 60 tables, enter the following valid Startup Parameter sequence in the "Startup Parameters" box or "Startup parameters" edit box:

-c15 -w125 -d60