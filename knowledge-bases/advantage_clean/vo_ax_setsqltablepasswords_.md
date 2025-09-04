---
title: Vo Ax Setsqltablepasswords
slug: vo_ax_setsqltablepasswords_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_setsqltablepasswords_.htm
source: Advantage CHM
tags:
  - vo
checksum: eb38309bd97c7937d1b009b2209622188069c489
---

# Vo Ax Setsqltablepasswords

AX\_SetSQLTablePasswords()

AX\_SetSQLTablePasswords()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_SetSQLTablePasswords()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Sets passwords for encrypted tables for use with the AXSQL RDDs.

Syntax

AX\_SetSQLTablePasswords ( [<aPasswords>] )

| <aPasswords> | A two dimensional array containing table/password string pairs. For example: {{ "customers", "password" }} or {{ "employees", "password1" }, {"accounts", "password2" }} |

Description

Sets the table passwords for any encrypted tables used in an SQL query. Once set, all subsequent queries will use the provided passwords. To un-set the passwords, simply call the function with an empty array. For example:

AX\_SetSQLTablePasswords( {} )

If the statement handle was created on a database connection, setting the encryption password for database tables is ignored. The database tables encryption password is stored in the database and automatically available to the authenticated users.

See Also

[AdsStmtSetTablePassword](ace_adsstmtsettablepassword.md)
