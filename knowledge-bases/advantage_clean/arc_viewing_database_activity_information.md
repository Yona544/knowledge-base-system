---
title: Arc Viewing Database Activity Information
slug: arc_viewing_database_activity_information
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_viewing_database_activity_information.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 90f1033e24aab2779810a3bcb813a7e0635a7b8c
---

# Arc Viewing Database Activity Information

Viewing Database Activity Information

Viewing Database Activity Information

Advantage Data Architect

| Viewing Database Activity Information  Advantage Data Architect |  |  |  |  |

The Database Information screen displays the current activity on the server.

Field Descriptions

Current

The current number of an item in use.

Max Used

The maximum number of resources actually in use at one time since the Advantage Database Server was loaded/started.

Note The "Max Used" information is provided to help system administrators fine-tune the configuration of the Advantage Database Server for optimal performance. For example, if after several days of active use, the maximum number of data locks in use at one time is 50, the system administrator could reconfigure the Advantage Database Server to allocate 55 data locks.

Configured

Shows the initial number of an item that the Advantage Database Server has available.

Rejected

Indicates that a configured value has been exceeded and the Advantage Database Server was unable to allocate more resources for additional items. If numbers frequently appear in this column, it is an indication that the configuration parameters should be increased or a larger user option should be purchased.

Users

A user is defined as a single client workstation connected to the Advantage Database Server. The number of users is not configurable. The Advantage Database Server option purchased determines the maximum number of users.

Connections

With Advantage DOS client applications, a connection is an individual application that can access the Advantage Database Server.

With Advantage Windows client applications, a connection is defined as an individual 16-bit application, an individual thread in a 32-bit application, or it can be obtained by a call to the specific Advantage Windows Client API to obtain a new connection. Each user can have multiple active connections.

Work Areas

A work area is a logical "container" that consists of a single open table, an optional memo file, and up to 15 index files.

Tables

A table in your database.

Index Files

An index file in your database.

Data Locks

A data lock is an individual record lock, table lock, index file lock, memo file lock, or table header lock.

Worker Threads

Advantage Database Server Worker Threads perform the actual database operations on the server.
