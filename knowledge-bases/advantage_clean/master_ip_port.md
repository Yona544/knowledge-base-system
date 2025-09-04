---
title: Master Ip Port
slug: master_ip_port
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ip_port.htm
source: Advantage CHM
tags:
  - master
checksum: 3357a7acb2a9dc4cfeac6f5883bd2ad0d373603b
---

# Master Ip Port

IP Port

IP Port

Advantage Database Server

| IP Port  Advantage Database Server |  |  |  |  |

Default = 0, which means that Advantage Database Server should attempt to bind to the default port of 6262.

The Advantage Database Server communicates with the Advantage JDBC client via TCP/IP and can communicate with Advantage Windows and Linux clients via either TCP/IP or UDP/IP. By default, for communication to Advantage applications that have connected to the Advantage Database Server via a "remote" connection (a.k.a. an ADS\_REMOTE\_SERVER connection), the Advantage Database Server will bind to all available IP addresses on the server and it will bind to port 6262 for each available IP address. The IP address and the IP port that the Advantage Database Server uses can be configured to specific values, however. See [LAN IP Address](master_lan_ip_address.md) for configuring the IP address, and use this IP Port setting for configuring the IP port.

For communication to Advantage Java clients using TCP/IP, if the default port of 6262 is unavailable, an error will be logged when the Advantage Database Server starts, and the Advantage Database Server will be unable to communicate to those clients. If you want the Advantage Database Server to use a specific TCP/IP port, rather than port 6262, edit the IP Port setting.

For communication to Advantage Windows and Linux clients using UDP/IP, if the default port of 6262 is unavailable, the next available IP port will be used. If you want the Advantage Database Server to use a specific TCP/IP port, rather than port 6262 or the next available port (should port 6262 not be available), edit the IP Port setting.

For Windows and Linux, the NETSTAT utility with the option "-a" (i.e., "netstat -a") can be used to find out what IP ports are currently in use.

The IP port used by the Advantage Database Server can be retrieved by using the AdsMgGetConfigInfo API or the sp\_MgGetConfigInfo system procedure. It is also displayed by the Advantage Management Utility within Advantage Data Architect (ARC), on the Configuration Parameters tab, in the Not Affecting Memory section.

Note: The maximum number of concurrent TCP connection to the Advantage Database Server is 3000. If more than 3000 concurrent connection to the server is required, the clients should be configured to use UDP communication.

See Also

[LAN IP Address](master_lan_ip_address.md)

[Internet IP Address](master_internet_ip_address.md)

[Internet Port](master_internet_port.md)
