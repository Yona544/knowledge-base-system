---
title: Master Installing Multiple Instances
slug: master_installing_multiple_instances
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_installing_multiple_instances.htm
source: Advantage CHM
tags:
  - master
checksum: 4738673c01a9c2dab0e92e9e3e0e77f2c8107481
---

# Master Installing Multiple Instances

Installing Multiple Instances on a Single Server

Installing Multiple Instances on a Single Server

Advantage Database Server

| Installing Multiple Instances on a Single Server  Advantage Database Server |  |  |  |  |

In some cases it is useful to install multiple versions of the Advantage Database Server (ADS) on a single physical server.  Typically this is done when multiple Advantage-enabled applications are using the same physical server, but are shipped using different versions of Advantage.  Starting with Advantage version 10, additional instances of Advantage can now be installed on the same physical server.

Any version of ADS can be the first installed instance of ADS on the server.  However, any additional instances of ADS installed must be version 10.0 or higher.  Also, any client applications wishing to use inter-process communication with an additional instance of ADS must use version 10.0 or higher of the Advantage Client Engine (ACE).

In order to install additional copies of ADS on one server, you must add some specific settings to the [setup.ini](master_performing_silent_installs.md) file of the server installation before running the install.

Discovery

Only the first ADS installation on a server will support discovery.  Any client applications relying on discovery to connect to ADS will only find the first ADS installation.  Clients that wish to connect to the additional ADS installation must specify the port number of that instance of ADS to connect to it.  The port number can be added to the connection path/string or specified in the client's ADS.INI file.

LAN and Internet Ports

When installing an additional instance of ADS, the LAN IP receive port number must be configured.  If no port is configured (or it is zero), ADS will use the first available port on the server.  Since additional ADS installations do not support discovery, the client will not be able to determine which port to connect to.  Also if you use internet connections with ADS, you must specify unique internet port numbers for each ADS installation.

Inter-process Communication

Inter-process Communication (IPC) is supported by all installations of ADS on a server.  However, the client must know the port number of the ADS installation if connecting to an additional instance.  If no port number is specified, the client will attempt to connect to the first installation of ADS on the server.

Error Log & TPS File Locations

The error log and TPS file location paths must be configured to be unique for each installation of ADS on the server.  By default the first ADS installation will use C:\ for Windows and /var/log/advantage for Linux.  Additional ADS installations will by default configure these paths to be the installation path of ADS.

Service Information (Windows only)

For ADS installations on Windows, each installation must have unique Windows service information.  The first installation will get the default service name Advantage.  Additional installations will use the service name specified in the setup.ini file during the installation process.  This service name must be configured in the setup.ini file for all additional instances of ADS installed.  See Installing Multiple Instances on a Single Server on Windows for more details.
