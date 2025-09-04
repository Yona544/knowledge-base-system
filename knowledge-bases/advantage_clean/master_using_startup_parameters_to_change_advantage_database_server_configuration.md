---
title: Master Using Startup Parameters To Change Advantage Database Server Configuration
slug: master_using_startup_parameters_to_change_advantage_database_server_configuration
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_using_startup_parameters_to_change_advantage_database_server_configuration.htm
source: Advantage CHM
tags:
  - master
checksum: fd751bde2531d0f24aaf54ca71e4e223ac13cc47
---

# Master Using Startup Parameters To Change Advantage Database Server Configuration

Using Startup Parameters to Change Advantage Database Server Configuration

Using Startup Parameters to Change Advantage Database Server Configuration

Advantage Database Server

| Using Startup Parameters to Change Advantage Database Server Configuration  Advantage Database Server |  |  |  |  |

To change the Advantage Database Server Service configuration using Startup Parameters, you must stop the Advantage Database Server Service and re-start it with new configuration parameters specified in the "Startup Parameters" box (with Windows NT 4.0) or "Start parameters" edit box (with Windows 2000/2003) located in the Service Control Manager.

Enter the desired configuration changes into the "Startup Parameters" box (with Windows NT 4.0) or "Start parameters" edit box (with Windows 2000/2003). For example, if you wish to change the Advantage Database Server service configuration to 15 connections, 125 work areas and 60 tables, enter the following valid Startup Parameter sequence in the "Startup Parameters" box or "Startup parameters" edit box:

-c15 -w125 -d60
