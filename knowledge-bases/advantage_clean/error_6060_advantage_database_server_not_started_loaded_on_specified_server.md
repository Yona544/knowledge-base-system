---
title: Error 6060 Advantage Database Server Not Started Loaded On Specified Server
slug: error_6060_advantage_database_server_not_started_loaded_on_specified_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6060_advantage_database_server_not_started_loaded_on_specified_server.htm
source: Advantage CHM
tags:
  - error
checksum: 7c2b51abd9366183562c438440eefeca984b64f0
---

# Error 6060 Advantage Database Server Not Started Loaded On Specified Server

6060 Advantage Database Server not started/loaded on specified server

6060 Advantage Database Server not started/loaded on specified server

Advantage Error Guide

| 6060 Advantage Database Server not started/loaded on specified server  Advantage Error Guide |  |  |  |  |

Problem 1: The Advantage Database Server is not started/loaded on the specified server.

Solution 1: Verify that the Advantage Database Server is started/loaded on the server. Make sure that the application is referencing the correct server.

Problem 2: An Advantage Windows client v2.6 or greater is being used, a connection is being attempted to a local drive, and the Advantage Database Server is not running on that local machine.

Solution 2: Verify that the Advantage Database Server is started on the local machine. If you are attempting to open the file via the Advantage Local Server, make sure that use of the Advantage Local Server has been enabled via the AdsSetServerType() API, the TAdsSettings.AdsServerTypes property, the TAdsConnection.AdsServerTypes property, or the ADS\_SERVER\_TYPES setting in the ads.ini file.

Linux Server Only

It is possible to receive a 6060 error if the Advantage for Linux daemon started, but had a problem registering for multicast discovery packets. If this happens you will find a detailed error message in the ads\_log.txt file.

Following are known issues that can cause this behavior:

- No default gateway is assigned. The server must have a default gateway or the multicast registration will not be successful.

- Some users have mentioned that they had to enable ip forwarding to resolve this issue.

Other Linux-specific issues that can cause a 6060 error include the following:

- Invalid or incorrect IP address in the /etc/hosts file.

- Incorrect hostname is assigned. Verify that the hostname returned by running the 'hostname' utility is the same as the name used in the connection string.

- If using Samba, verify that the directory you are sharing is located directly off of the root. For example the samba share \\testserv\myshare must be sharing the /myshare directory.
