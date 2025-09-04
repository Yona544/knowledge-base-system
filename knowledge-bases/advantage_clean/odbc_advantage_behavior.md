---
title: Odbc Advantage Behavior
slug: odbc_advantage_behavior
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_advantage_behavior.htm
source: Advantage CHM
tags:
  - odbc
checksum: 118fbca3ce49e12e082ae692bf2b5b12349b8f95
---

# Odbc Advantage Behavior

Advantage Behavior

Advantage Behavior

Advantage ODBC Driver

| Advantage Behavior  Advantage ODBC Driver |  |  |  |  |

When Advantage is selected as the [table type](odbc_table_type.md), the default extension used for tables is ADT, and the extension for created indexes is ADI. The ADI indexes created are auto-open. In this case, they are automatically selected and no additional Data Source setup is required.

When creating indexes, "tags" (similar to individual index files) are added to the auto-open index. If an auto-open index does not exist, one will be created and the tag will be inserted.
