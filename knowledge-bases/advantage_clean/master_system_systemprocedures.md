---
title: Master System Systemprocedures
slug: master_system_systemprocedures
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_systemprocedures.htm
source: Advantage CHM
tags:
  - master
checksum: 3cd9b8ff7c7e2dd8195d1f1bbb0bab6bf80ee8c3
---

# Master System Systemprocedures

system.systemprocedures

system.systemprocedures

Advantage SQL Engine

| system.systemprocedures  Advantage SQL Engine |  |  |  |  |

Contains one row for each system procedure (sometimes referred to as "canned procedure") in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | System procedure name. |
| Proc\_Input | Memo | variable | Input parameters to the system procedure in AdsCreateTable format. |
| Proc\_Output | Memo | variable | Output parameters for the system procedure in AdsCreateTable format. |
| Comment | Memo | variable | The description of the system procedure. |
