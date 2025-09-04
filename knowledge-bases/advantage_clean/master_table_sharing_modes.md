---
title: Master Table Sharing Modes
slug: master_table_sharing_modes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_table_sharing_modes.htm
source: Advantage CHM
tags:
  - master
checksum: d1089f68e74c4375a330bf3a76c0b5d58acd747d
---

# Master Table Sharing Modes

Table Sharing Modes

Table Sharing Modes

Advantage Concepts

| Table Sharing Modes  Advantage Concepts |  |  |  |  |

Tables can be opened in one of two sharing modes: exclusive or shared. Opening a table in Exclusive mode gives only one application access to the table. Opening a table in Shared mode gives other applications on the network access to the table. In order for multiple applications to share common data, they must all specify that the file is to be opened in Shared mode.

Existing index files and memo files are always opened in the same sharing mode as the associated table. For example, if a table is opened in Exclusive mode, then an index file opened on that table will also be opened in Exclusive mode. All newly created tables and index files are automatically created and remain open in Exclusive mode.
