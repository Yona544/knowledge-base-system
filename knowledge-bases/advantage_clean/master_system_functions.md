---
title: Master System Functions
slug: master_system_functions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_functions.htm
source: Advantage CHM
tags:
  - master
checksum: 4b678f38f1589cb2649bd459a5b5557996ae4b7b
---

# Master System Functions

system.functions

system.functions

Advantage SQL Engine

| system.functions  Advantage SQL Engine |  |  |  |  |

Contains one row for each function in the database.

| Field Name | Field Type | Field Size | Description |
| Name | CICharacter | 200 | Function name. |
| Package | CICharacter | 200 | Name of the package that the function is part of. May be NULL or empty string. |
| Return Type | CICharacter | 20 | Data type of the function. |
| Input Parameters | Memo | Variable | Input parameters in comma separated list. |
| Implementation | NMemo | Variable | The SQL script that implements the function. |
| Comment | Memo | Variable | Function description. |
| User\_Defined\_Prop | Blob | Variable | Inaccessible at the moment. |
