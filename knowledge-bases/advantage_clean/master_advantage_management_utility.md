---
title: Master Advantage Management Utility
slug: master_advantage_management_utility
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_management_utility.htm
source: Advantage CHM
tags:
  - master
checksum: faf574576776b134026c0af01cf30b01eeef34e8
---

# Master Advantage Management Utility

Advantage Management Utility

Advantage Management Utility

Advantage Database Server

| Advantage Management Utility  Advantage Database Server |  |  |  |  |

The Advantage Management Utility is a 32-bit end-user database management utility that provides access to Advantage Database Server management information. Using this utility, networked client PCs can access management information on servers running the Advantage Database Server. The Advantage Management Utility brings the convenience of watching Advantage Database Server activity information to your client machine. This aids in development, troubleshooting, and performance monitoring which, in turn, increases productivity.

The Advantage Management Utility has been incorporated into the [Advantage Data Architect](master_advantage_data_architect.md). However, a stand-alone version is also available from the Downloads/Tools & Utilities section of the Advantage Developer Zone Web site at: http://DevZone.AdvantageDatabase.com.

Through a persistent connection to the Advantage Database Server, the Advantage Management Utility allows you to:

- Browse general database activity information

- Check installation information

- View connected users

- View open files

- Check configuration parameters that do and do not affect server memory

- View communication statistics

Database Information

The Database Information screen includes rows for some of the main database items: Users, Connections, Work Areas, Tables, Index Files, Data Locks, and Worker Threads.

Installation Information

The Installation Information screen includes information that is entered/calculated when the Advantage Database Server is installed.

Connected Users

The Connected Users screen displays a list of all connected users. The User Information displayed includes the users computer name, the users data dictionary user name (if applicable), and the users network address.

Open Files

The Open Files screen displays the currently open data files or index files. Preceding the file name is the locking method used to open the file with Advantage.

Configuration Parameters Affecting Memory

The Configuration Parameters Affecting Memory screen shows the currently loaded parameters affecting memory when the Advantage Database Server is loaded.

Configuration Parameters Not Affecting Memory

The Configuration Parameters Not Affecting Memory screen displays the current parameters that are defined at load time but have no direct effect on file server memory usage.

Communication Statistics

The Communication Statistics screen shows the packet and low level network status.
