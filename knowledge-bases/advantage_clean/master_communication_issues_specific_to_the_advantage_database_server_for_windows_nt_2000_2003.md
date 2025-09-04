---
title: Master Communication Issues Specific To The Advantage Database Server For Windows Nt 2000 2003
slug: master_communication_issues_specific_to_the_advantage_database_server_for_windows_nt_2000_2003
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_communication_issues_specific_to_the_advantage_database_server_for_windows_nt_2000_2003.htm
source: Advantage CHM
tags:
  - master
checksum: 2f1d2f5aa34479df481e2cd84d61e2cb9946086c
---

# Master Communication Issues Specific To The Advantage Database Server For Windows Nt 2000 2003

Communication Issues Specific to the Advantage Database Server for Windows

Communication Issues Specific to the Advantage Database Server for Windows

Networking Issues

| Communication Issues Specific to the Advantage Database Server for Windows  Networking Issues |  |  |  |  |

In general, if you can map a drive to the server on which the Advantage Database Server for Windows is running, you should be able to run an Advantage application. If communication to the Advantage Database Server for Windows is not working, you should check if the network protocol being used is actually working on both the client and server computers.

IPX Communication Issues

If the network protocol to be used is IPX, there are a few things you can do to verify IPX is working correctly. Verify the IPX frame types and the network number is the same on the client computer(s) and the server computer. This information is available via the Network icon in the Control Panel folder under the IPX/SPX protocol properties. If the frame type and network number are the same, you can map a drive to the server, but Advantage communication is still not working, you should verify IPX is really working by temporarily removing or disabling all other protocols, like IP and NetBEUI, on the client computer. Do not disable NetBIOS, however. Once the other protocols are removed/disabled, you can verify IPX is working by attempting to map a drive again. If this is successful, your Advantage application should also be able to communicate with the Advantage Database Server for Windows.

IP Communication Issues

If the network protocol to be used is IP, there are a few things you can do to verify IP is working correctly. From the client computer, ping the server computer by running PING.EXE <server name>. If ping does not successfully find the server, then IP is not set up properly. To view IP configuration on a Windows 95, Windows 98, or Windows ME computer, run WINIPCFG.EXE. To view IP configuration on a Windows computer, run IPCONFIG.EXE.

Overriding Protocol Auto-Sense

The Advantage Windows communication layers auto-sense for which protocol is available for communication. If both IP and IPX are available on the client and server computers, IP will automatically be used. If only one is available, that protocol will be used. If both IP and IPX are available, it is possible to force one or the other to be used. The DEFAULT\_PROTOCOL value in the ADS.INI file changes the default network protocol to use when the Advantage client communicates with the Advantage Database Server. If the DEFAULT\_PROTOCOL setting is 1, then IPX will be the preferred protocol. If the setting is any other value, then IP will be the preferred protocol. If you wanted your Advantage application to use IPX as the preferred or default protocol, then you need to create an ADS.INI file that contains the entry:

[SETTINGS]

DEFAULT\_PROTOCOL = 1

Some developers have found IPX communication to be faster than IP communication at their sites. The converse is also true. Some customers have found IP communication to be faster than IPX communication. If you have both IPX and IP protocols available at your site or your customer's site, and you are having performance problems with your Advantage application, you may want to try forcing one or the other protocol to be used and run some performance tests.

10000 Errors

Some third-party products install a customized Winsock DLL. If your Advantage application is receiving 10000 error numbers, verify your Winsock DLL is a standard Microsoft DLL.

Firewall Communication Issues

If a firewall exists between your client computer and the server computer, you may have IP communication problems with Advantage. One port must be opened in your firewall to allow Advantage IP communication to be successful. This port is used for data sent between the Advantage client and the Advantage Database Server. This port number is configurable in the Advantage Database Server via the Advantage Configuration Utility for the Advantage Database Server for Windows.
