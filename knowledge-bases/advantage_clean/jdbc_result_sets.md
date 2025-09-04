---
title: Jdbc Result Sets
slug: jdbc_result_sets
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_result_sets.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 3876650496dc5059324ee70a928df21cfa712383
---

# Jdbc Result Sets

Result Sets

Result Sets

Advantage JDBC Driver

| Result Sets  Advantage JDBC Driver |  |  |  |  |

The Advantage JDBC Driver supports scroll-insensitive, scroll-sensitive, updateable and read only result sets. The type and concurrency of the result set corresponds the type of cursor returned by the Advantage SQL engine. Advantage SQL engine returns 2 types of cursors, live and static. Their corresponding JDBC result set type and concurrency is listed in the following table. For more information on Advantage cursor type, see [Live versus Static Cursors](master_live_versus_static_cursors.md).

| Advantage Cursor Type | JDBC Result Set |
| Live | scroll-sensitive, updatable/readonly |
| Static | scroll-insensitive, readonly |

When the Advantage JDBC driver cannot support the requested result set type or concurrency, it automatically downgrades the result set and generates one or more SQLWarnings with additional information.
