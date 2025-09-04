---
title: Master Drop Table
slug: master_drop_table
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_drop_table.htm
source: Advantage CHM
tags:
  - master
checksum: d47f650bbb7c24e92b72abceafd3e15705957cc5
---

# Master Drop Table

DROP TABLE

DROP TABLE

Advantage SQL Engine

| DROP TABLE  Advantage SQL Engine |  |  |  |  |

Deletes a table and any indexes associated with it from the database

Syntax

DROP TABLE <table-name> [FROM DATABASE [NO\_DELETE]]

 

Remarks

CASCADE, RESTRICT not supported.

If the table is a database table), that is, if the table is associated with an [Advantage Data Dictionary](master_advantage_data_dictionary.md), the table can only be deleted if the DROP TABLE statement is executed by a user with DROP permissions on the specified table. The NO\_DELETE option will cause a database table to be removed from the data dictionary, but not deleted from disk. The FROM DATABASE clause is not required to drop a database table, however, it is required to specify the NO\_DELETE option.

Note Encrypted database tables removed from the database, but not deleted, will be left in a decrypted state.

Example(s)

DROP TABLE sal

DROP TABLE sal FROM DATABASE NO\_DELETE
