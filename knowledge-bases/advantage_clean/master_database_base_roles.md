---
title: Master Database Base Roles
slug: master_database_base_roles
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_database_base_roles.htm
source: Advantage CHM
tags:
  - master
checksum: ad8bd1f686495d805f309e056e14f566f77bf95f
---

# Master Database Base Roles

Database Roles

Database Roles

Advantage Database Server

| Database Roles  Advantage Database Server |  |  |  |  |

In addition to the more flexible user groups that can be defined and customized infinitely by developer or end user, Advantage now supports predefined user groups (roles) in the database. They are DB:Admin, DB:Backup, DB:Debug DB:Public, SERVER:Admin, and SERVER:Monitor.

The first three groups have predefined permission that cannot be changed. Membership of the groups are not predefined but can be assigned by ADSSYS user or members of the DB:Admin group.

Members of the DB:Admin group has the identical permission as the ADSSYS user, except the permission to change the ADSSYS password.

Members of the DB:Backup group has the permission to execute the sp\_BackupDatabase() and sp\_BackupFreeTables() stored procedures.

Members of the DB:Debug group has the permission to debug SQL scripts executing on any connection to the database, and the permission to modify any trigger, stored procedure or user defined function in the database.

The fourth group, DB:Public, has no predefined permission but it includes as members all users in the database. Specific permission on individual database object may be granted to the DB:Public group, thus making the permission available to all users in the database. For example, if one of the table should be readable by all users in the database, then the READ permission on the table may be granted to the DB:Public group instead of granting to the individual users. Because the DB:Public group always includes all users, any newly created user will automatically get the READ permission to the table.

Members of the SERVER:Admin group acquire certain permissions when connected to the [root dictionary](master_root_dictionary.md). You can run the following query to list the procedures that require SERVER:Admin membership when run on the root dictionary:

SELECT name FROM system.systemprocedures WHERE required\_permissions & 2 = 2

Members of the SERVER:Monitor group acquire certain permissions when connected to the [root dictionary](master_root_dictionary.md). You can run the following query to list the procedures that require SERVER:Monitor membership when run on the root dictionary:

SELECT name FROM system.systemprocedures WHERE required\_permissions & 4 = 4

See Also

[Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md)
