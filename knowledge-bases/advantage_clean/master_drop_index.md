---
title: Master Drop Index
slug: master_drop_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_drop_index.htm
source: Advantage CHM
tags:
  - master
checksum: ae056afc325e7a7e4911353e5a94904378dc6e95
---

# Master Drop Index

DROP INDEX

DROP INDEX

Advantage SQL Engine

| DROP INDEX  Advantage SQL Engine |  |  |  |  |

Deletes index orders (tags) from a CDX or ADI index file. When the last index order is deleted in an index file, the index file is deleted.

Syntax

DROP INDEX <table-name>.<index-name>

Remarks

If the table is a database table), that is, if the table is associated with an [Advantage Data Dictionary](master_advantage_data_dictionary.md), the DROP INDEX statement can only be executed from a user with ALTER permissions on the specified indexs associated table.

Example(s)

DROP INDEX emp.empid
