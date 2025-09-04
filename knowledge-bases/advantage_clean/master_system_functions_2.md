---
title: Master System Functions 2
slug: master_system_functions_2
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_functions_2.htm
source: Advantage CHM
tags:
  - master
checksum: dfcf0d8fef68fed4ed03eb691c38ba2f35528178
---

# Master System Functions 2

system.ansi\_functions

system.ansi\_functions

Advantage SQL Engine

| system.ansi\_functions  Advantage SQL Engine |  |  |  |  |

Contains one row for each function in the database.

| Field Name | Field Type | Field Size | Description |
| Name | CICharacter | 200 | Function name. |
| Package | CICharacter | 200 | Name of the package that the function is part of. May be NULL or empty string. |
| Return Type | CICharacter | 20 | Data type of the function. |
| Input Parameters | Memo | Variable | Input parameters in comma separated list. |
| Implementation | Memo | Variable | The SQL script that implements the function. |
| Comment | Memo | Variable | Function description. |
| User\_Defined\_Prop | Blob | Variable | Inaccessible at the moment. |
