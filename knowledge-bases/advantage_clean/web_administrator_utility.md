---
title: Web Administrator Utility
slug: web_administrator_utility
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_administrator_utility.htm
source: Advantage CHM
tags:
  - web
checksum: 20e3fb71ac8e879f7f0ed04ab1a0e9a59068faf2
---

# Web Administrator Utility

Advantage Web Administrator Utility

Advantage Web Administrator Utility

Advantage Web Platform

| Advantage Web Administrator Utility  Advantage Web Platform |  |  |  |  |

The Advantage Web Administrator provides the capability to monitor one or more Advantage Database Server installations from remote locations. It is a web application developed with JavaScript and runs against the [Advantage Web Platform](web_advantage_web_platform.md).

The Advantage Web Administrator shares some functionality with Advantage Data Architect in that it allows you to view server configuration information, connected users, and provides the ability to run ad-hoc queries. It is intended to be an additional tool for administering and monitoring ADS installations rather than a replacement for Advantage Data Architect.

Some of the current functionality includes

- View a summary of the high level database information (number of users, connections, open tables, etc.)

- View installation details

- View list of connected users

- Disconnect selected users

- Enable and disable logins for a database

- View list of open tables and indexes

- View list of active queries.

- Cancel selected queries.

- Control query logging (and view the query log)

- View a list of crash dump files on the server (if they exist)

- View error log entries

- Run ad-hoc SQL queries

The ability to run queries depends on the query service ([DbEnableQueryService](web_installing_the_awp.md)) being enabled in the Advantage Web Platform. More information about this is [available here](web_administrator_setup.md).

This version of the administrator utility also provides the capability to set some of the Advantage configuration values remotely. However, some of these values still require the Advantage server to be restarted for them to take effect. See [sp\_mgSetConfigValue](master_sp_mgsetconfigvalue.md) for details.
