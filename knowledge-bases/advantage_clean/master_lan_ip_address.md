---
title: Master Lan Ip Address
slug: master_lan_ip_address
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_lan_ip_address.htm
source: Advantage CHM
tags:
  - master
checksum: 013eb98c724ec67475346016a72566352a7e6281
---

# Master Lan Ip Address

LAN IP Address

LAN IP Address

Advantage Database Server

| LAN IP Address  Advantage Database Server |  |  |  |  |

Default = All IP addresses on the machine

The Advantage Database Server communicates with the Advantage JDBC client via TCP/IP and can communicate with Advantage Windows and Linux clients via UDP/IP. By default, for communication to Advantage applications that have connected to the Advantage Database Server via a "remote" connection (a.k.a. an ADS\_REMOTE\_SERVER connection), the Advantage Database Server will bind to all available IP addresses on the server and it will bind to port 6262 for each available IP address. The IP address and the IP port in which the Advantage Database Server uses can be configured to specific values, however. See [IP Port](master_ip_port.md) for configuring the IP port, and use this LAN IP Address setting for configuring a specific IP address.

When an IP address is not specified, all IP addresses will be used. In most cases, modifying this LAN IP Address setting is not needed since machines only have one IP address. On multihomed machines (machines with more than one IP address), this setting can be used to force the Advantage Database Server to use a specific address. For Microsoft Windows clustering support, the IP address needs to be set to the Cluster IP address.

Note that if an invalid address is specified, the Advantage Database Server will fail when binding to that address. This will cause the IP protocol to not be available for "remote" (a.k.a. an ADS\_REMOTE\_SERVER). An invalid address will cause a 10047 Winsock error to be logged in the Advantage error log when the Advantage Database Server is started. Also note that this setting should only be used with a static IP address.

To set a specific IP address, perform one of the following where "xxx.xxx.xxx.xxx" is replaced by the actual IP address.

For Windows:

Add the following string value using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\LAN\_IP\_ADDRESS=xxx.xxx.xxx.xxx

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf):

LAN\_IP\_ADDRESS=xxx.xxx.xxx.xxx

See Also

[IP Port](master_ip_port.md)

[Internet IP Address](master_internet_ip_address.md)

[Internet Port](master_internet_port.md)
