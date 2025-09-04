---
title: Master Using Table Names With Paths
slug: master_using_table_names_with_paths
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_using_table_names_with_paths.htm
source: Advantage CHM
tags:
  - master
checksum: 8875b0324fceeb5f6daa359ce77aa8db2c0c91f0
---

# Master Using Table Names With Paths

Using Table Names with Paths

Using Table Names with Paths

Advantage SQL Engine

| Using Table Names with Paths  Advantage SQL Engine |  |  |  |  |

Drive letters in paths of table names can only be used with Advantage Local Server. When using Advantage Database Server for NT, fully qualified paths must use UNC (e.g., "\\server\volume\path\table"), because the SQL statement is parsed at the server where client-side drive letters are not meaningful. Note that tables referenced like this must be enclosed in double quotes or [] (brackets) because they contain non-standard characters (see [Use of Non-Standard Characters in Names](master_use_of_non_standard_characters_in_names.md)).

If relative paths are used in SQL statements, the path is considered to be relative to the connection path. For example, a table referenced as "..\alternate\info" would refer to a directory named "alternate" that would be expected to be parallel to the original connection path directory.
