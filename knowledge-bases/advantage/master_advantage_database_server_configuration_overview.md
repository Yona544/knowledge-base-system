Advantage Database Server Configuration Overview




Advantage Database Server 12  

Advantage Database Server Configuration Overview

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Database Server Configuration Overview  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Advantage Database Server Configuration Overview Advantage Database Server master\_Advantage\_database\_server\_configuration\_overview Advantage Database Server > Advantage Database Server Configuration > Overview / Dear Support Staff, |  |
| Advantage Database Server Configuration Overview  Advantage Database Server |  |  |  |  |

The Advantage Database Server can be configured in a variety of ways to fine-tune the Advantage Database Server to more effectively use the server resources and to gain optimal performance. This section describes the configuration information accessible with the Advantage Database Server. A configuration file is provided with the Advantage Database Server for Linux to ease in assigning and re-using configuration parameters. For the Advantage Database Server for Windows, configuration information is stored in the Windows Registry.

The CONNECTIONS, WORKAREAS, TABLES, INDEXES, and LOCKS configuration parameters control the initial amount of resources Advantage will allocate at startup. Should Advantage run out of available connections, tables, etc., it will allocate more resources to accommodate more open connections, tables, etc. Later, if those extra resources are not being used, Advantage will free them and reduce the number of available connections, tables, etc.

Note Advantage will always keep at least the configured number of resources available for use. If via the Advantage Configuration Utility or the Advantage Management Utility you notice that the Max Used value of a resource is much greater than the Configured value, it is recommended that you increase the configured value of that resource. Changing a configuration parameter in the configuration file or registry requires the Advantage server to be restarted for the change to take effect.

[Advantage Database Server Configuration for Windows](master_advantage_database_server_configuration_for_windows_nt_2000_2003.htm)

[Advantage Database Server Configuration for Linux](master_advantage_database_server_configuration_for_linux.htm)