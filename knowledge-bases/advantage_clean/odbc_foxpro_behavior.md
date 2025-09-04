---
title: Odbc Foxpro Behavior
slug: odbc_foxpro_behavior
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_foxpro_behavior.htm
source: Advantage CHM
tags:
  - odbc
checksum: 42573bca048404a1e0be6c964776b2aaa914021f
---

# Odbc Foxpro Behavior

FoxPro Behavior

FoxPro Behavior

Advantage ODBC Driver

| FoxPro Behavior  Advantage ODBC Driver |  |  |  |  |

If the [Table Type](odbc_table_type.md) is FoxPro or Visual FoxPro, structural CDX indexes (those indexes which have the same base names as the database files) are opened implicitly. In this case they are automatically selected and no additional Data Source setup is required.

When creating indexes, "tags" (similar to individual index files) are added to the structural index. If a structural index does not exist, one will be created and the tag will be inserted.
