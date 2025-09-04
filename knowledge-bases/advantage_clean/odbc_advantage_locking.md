---
title: Odbc Advantage Locking
slug: odbc_advantage_locking
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_advantage_locking.htm
source: Advantage CHM
tags:
  - odbc
checksum: 6bbd22c907acb2e371c511929203a9df55a6d816
---

# Odbc Advantage Locking

Advantage Locking

Advantage Locking

| Advantage Locking |  |  |  |  |

Advantage locking may be set to Proprietary or Compatible.

Advantage Database Server, as default, maintains all locking control through a proprietary locking system. The Advantage locking system allows Advantage to be more efficient to provide better performance gains. It requires all applications sharing the database files to also be Advantage applications. If non-Advantage applications must share DBF data with Advantage applications, Advantage locking must be set to Compatible. When using Advantage-proprietary ADT tables, proprietary locking is always used. When using Advantage Local Server, this setting is ignored.
