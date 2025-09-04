---
title: Arc Viewing Configuration Parameters Affecting Memory
slug: arc_viewing_configuration_parameters_affecting_memory
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_viewing_configuration_parameters_affecting_memory.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 66d2db75d3f5bff724414f7a3b3f724618678092
---

# Arc Viewing Configuration Parameters Affecting Memory

Viewing Configuration Parameters Affecting Memory

Viewing Configuration Parameters Affecting Memory

Advantage Data Architect

| Viewing Configuration Parameters Affecting Memory  Advantage Data Architect |  |  |  |  |

Many Advantage Database Server configuration parameters affect CPU and memory usage, and altering the default settings may affect memory requirements on your server.

The Configuration Parameters Affecting Memory screen shows the currently loaded parameters affecting memory when the Advantage Database Server is loaded.

Field Descriptions

Number of Connections

This is the initial number of connections that can be active at one time.

- With Advantage DOS client applications, a connection is an individual application that can access the Advantage Database Server.

- With Advantage Windows client applications, a connection is defined as an individual 16-bit application, an individual thread in a 32-bit application, or it can be obtained by a call to the specific Advantage Windows Client API to obtain a new connection.

Each user can have multiple active connections.

Number of Work Areas

This is the initial number of work areas that can be in use at any one time. This number is the total sum of all work areas being used by all clients. A work area is a logical "container" that consists of a single open table, optional memo file, and up to 15 index files.

Number of Tables

This is the initial number of different tables that can be open at one time. This number cannot be larger than the number of configured work areas. However, due to the sharing of file handles, this number can be less than the number of work areas.

Number of Indexes

This is the initial number of index files that can be open at any one time.

Number of Data Locks

This is the initial number of record locks, table locks, implicit header locks, and implicit index locks that can be in effect at one time.

Number of Worker Threads

This is the number of Advantage Database Server worker threads used to service client database file requests. Adjusting the number of worker threads controls CPU dedication to the Advantage Database Server.

Memory (Bytes)

This is the amount of memory consumed by each configuration parameter. Each value contains the total memory (in bytes) for each setting. To determine how much memory is required per setting, divide the memory size by the number configured.

Total

The total amount of memory being used for all configuration parameters.

See Also

[Viewing Configuration Parameters Not Affecting Memory](arc_viewing_configuration_parameters_not_affecting_memory.md)
