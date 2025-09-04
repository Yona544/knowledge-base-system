Internet Port




Advantage Database Server 12  

Internet Port

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Internet Port  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Internet Port Advantage Database Server master\_Internet\_port Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Internet Port  Advantage Database Server |  |  |  |  |

Default = 0

The Advantage Database Server can communicate over the Internet with the Advantage JDBC client via TCP/IP and can communicate over the Internet with Advantage Windows and Linux clients via either TCP/IP or UDP/IP. See [Advantage Internet Server Overview](master_advantage_internet_server_overview.htm) for details. The default value of 0 for this Internet Port setting means Internet access to the Advantage Database Server is disabled. To enable Internet access to the Advantage Database Server, a non-zero value must be specified for this Internet Port. Once this Internet Port is specified, by default the Advantage Database Server will bind to all available IP addresses on the server and it will bind to the specified port for each available IP address. This allows for communication to Advantage applications that have connected to the Advantage Database Server via an "Internet" connection (a.k.a. an ADS\_INTERNET\_SERVER connection). The IP address used for Internet communication with the Advantage Database Server can be configured to a specific value. See [Internet IP Address](master_internet_ip_address.htm) for more information. As mentioned above, use this Internet Port setting to specify the IP port used for Internet communication.

For Windows and Linux, the NETSTAT utility with the option "-a" (i.e., "netstat -a") can be used to find out what IP ports are currently in use.

An Advantage Internet connection requires an [Advantage Data Dictionary](master_advantage_data_dictionary.htm) be created and may also require a valid user name and password be configured before a connection will be granted. This ensures that the connection to the Advantage Database Server through the Internet port is secure and properly authenticated. In a normal scenario, to protect the Advantage Database Server from unauthorized access, the "remote" (a.k.a. an ADS\_REMOTE\_SERVER) [IP Port](master_ip_port.htm) should be blocked from access through Internet by a Firewall. While this Internet IP port can be opened through the Firewall knowing that the Advantage Database server will authenticate the connection.

The internet port used by the Advantage Database Server can be retrieved by using the AdsMgGetConfigInfo API or the sp\_MgGetConfigInfo system procedure. It is also displayed by the Advantage Management Utility within Advantage Data Architect (ARC), on the Configuration Parameters tab, in the Not Affecting Memory section.

Note: The maximum number of concurrent TCP connection to the Advantage Database Server is 3000. If more than 3000 concurrent connection to the server is required, the clients should be configured to use UDP communication.

See Also

[Internet IP Address](master_internet_ip_address.htm)

[LAN IP Address](master_lan_ip_address.htm)

[IP Port](master_ip_port.htm)