---
title: Master Associating Indexes With Tables
slug: master_associating_indexes_with_tables
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_associating_indexes_with_tables.htm
source: Advantage CHM
tags:
  - master
checksum: 4c6ef6544808e02cb6f5b416ae978e9c3bb435dc
---

# Master Associating Indexes With Tables

Associating Indexes with Tables

Associating Indexes with Tables

Advantage SQL Engine

| Associating Indexes with Tables  Advantage SQL Engine |  |  |  |  |

If SQL statements are used on free connections (connections that are not associated with an Advantage Data Dictionary), the SQL engine only uses auto-open index files (those with the same base name as the table) because the SQL engine does not know the names of the index files. To use indexes other than auto-open indexes, use a Database Connection, which is a connection made to Advantage Database Server or Advantage Local Server using an Advantage Data Dictionary file as the connection path. The data dictionary, among other functions, associates tables to index files.
