---
title: Master Drop Package
slug: master_drop_package
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_drop_package.htm
source: Advantage CHM
tags:
  - master
checksum: cf440415e67bf459894d9d0f1d9a7e73a0b9a63b
---

# Master Drop Package

DROP PACKAGE

DROP PACKAGE

Advantage SQL Engine

| DROP PACKAGE  Advantage SQL Engine |  |  |  |  |

Removes a package and its functions from the database.

Syntax

DROP PACKAGE package\_name

 

package\_name ::= identifier

 

Remark

The DROP PACKAGE statement removes the specified package from the database the database. All functions owned by the package are also removed.

The user must have the DROP permission on the specified package (see [GRANT](master_grant.md)).

Example

DROP PACKAGE StringFunctions;

 

See Also

[ALTER FUNCTION](master_alter_function.md)

[CREATE FUNCTION](master_create_function.md)

[CREATE PACKAGE](master_create_package.md)

[DROP FUNCTION](master_drop_function.md)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.md)
