---
title: Master Internet Ip Address
slug: master_internet_ip_address
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_internet_ip_address.htm
source: Advantage CHM
tags:
  - master
checksum: ffb03526b1173f7eab7aa524331c28862dc50416
---

# Master Internet Ip Address

Internet IP Address

Internet IP Address

Advantage Database Server

| Internet IP Address  Advantage Database Server |  |  |  |  |

Default = All IP addresses on the machine

The Advantage Database Server can communicate over the Internet to the JDBC client via TCP/IP and can communicate over the Internet to Windows and Linux clients via UDP/IP. See [Advantage Internet Server Overview](master_advantage_internet_server_overview.md) for details. By default the Advantage Database Server will bind to all available IP addresses on the server and it will bind to the specified port for each available IP address. This allows for communication to Advantage applications that have connected to the Advantage Database Server via an "Internet" connection (a.k.a. an ADS\_INTERNET\_SERVER connection). See [Internet Port](master_internet_port.md) for information on enabling Internet access to the Advantage Database Server and configuring the IP port used for Internet communication. Use this Internet IP Address setting for configuring a specific Internet IP address.

When an Internet IP address is not specified, all IP addresses will be used. In most cases, modifying this Internet IP Address setting is not needed since machines only have one IP address. On multihomed machines (machines with more than one IP address), this setting can be used to force the Advantage Database Server to use a specific address. For Microsoft Windows clustering support, the Internet IP address needs to be set to the Cluster IP address.

Note that if an invalid address is specified, the Advantage Database Server will fail when binding to that address. This will cause Internet access to the Advantage Database Server for "Internet" (a.k.a. an ADS\_INTERNET\_SERVER) connections to not be available. An invalid address will cause a 10047 Winsock error to be logged in the Advantage error log when the Advantage Database Server is started. Also note that this setting should only be used with a static IP address.

To set a specific Internet IP address, perform one of the following where "xxx.xxx.xxx.xxx" is replaced by the actual IP address.

For Windows:

Add the following string value using the Registry Editor (REGEDIT.EXE) into the registry.

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\INTERNET\_IP\_ADDRESS=xxx.xxx.xxx.xxx

See Also

[Internet Port](master_internet_port.md)

[LAN IP Address](master_lan_ip_address.md)

[IP Port](master_ip_port.md)
