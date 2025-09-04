---
title: Master Create Package
slug: master_create_package
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_create_package.htm
source: Advantage CHM
tags:
  - master
checksum: 7ec2b4277267a662549d30b80e29a70477f01b7e
---

# Master Create Package

CREATE PACKAGE

CREATE PACKAGE

Advantage SQL Engine

| CREATE PACKAGE  Advantage SQL Engine |  |  |  |  |

Creates a new package in the database.

Syntax

CREATE PACKAGE package\_name [DESCRIPTION package\_description]

 

package\_name ::= identifier

package\_description ::= string-literal

 

Remark

The CREATE PACKAGE statement creates a package in the database. Packages provide independent name spaces for the functions in the database. Functions with identical names may exists in the database as long as they are own by different package (see [CREATE FUNCTION](master_create_function.md)).

The user must have the CREATE PACKAGE permission to create a package in the database (see [GRANT](master_grant.md)).

Functions in a package do not have individual permissions. A users permission on the functions in the package is derived from the users permission on the package.

Example

 

CREATE PACKAGE StringFunctions;

CREATE PACKAGE MyFunc DESCRIPTION 'My functions';

See Also

[ALTER FUNCTION](master_alter_function.md)

[CREATE FUNCTION](master_create_function.md)

[DROP FUNCTION](master_drop_function.md)

[DROP PACKAGE](master_drop_package.md)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.md)
