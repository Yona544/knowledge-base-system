---
title: Odbc Database Directory
slug: odbc_database_directory
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_database_directory.htm
source: Advantage CHM
tags:
  - odbc
checksum: ff6cb2c2da07e7d05a9b6a17cb3a20451ad46918
---

# Odbc Database Directory

Database Directory

Database Directory

Advantage ODBC Driver

| Database Directory  Advantage ODBC Driver |  |  |  |  |

For free connections), a directory must be selected as the Database or Data Dictionary Path for the Advantage ODBC Driver to reference (e.g., x:\data). All free tables) in the directory will be available to the driver.

By specifying a directory as the Database or Data Dictionary Path for free connections), this implies that the directory is a database. When referencing information about databases using the Advantage ODBC Driver for free connections, you may substitute directory for the references to database.

Tables can be in different directories than the Database or Data Dictionary Path directory for free connections) by giving a fully-qualified path (either UNC or path with a drive letter) for a table name. The USE statement can be used to change the default database directory for free connections.

For database connections), it should be a valid path name including the Advantage Data Dictionary file name (e.g., x:\database\mydictionary.add).
