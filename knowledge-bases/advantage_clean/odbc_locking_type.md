---
title: Odbc Locking Type
slug: odbc_locking_type
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_locking_type.htm
source: Advantage CHM
tags:
  - odbc
checksum: 12293940ee30159110fa88f8b8cf36926e67b191
---

# Odbc Locking Type

Locking Type

Locking Type

| Locking Type |  |  |  |  |

Record or File locking may be specified as the default when handling the database files. When locks are established, to update data for example, either a record can be locked in the database file or the entire file may be locked.

Establishing the Locking setting is largely a performance issue. In most cases, record locking provides good performance while still maintaining concurrency control. However, if a large number of records are being updated in one file, file locks allow the updates to be performed faster.
