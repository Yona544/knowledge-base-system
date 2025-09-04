---
title: Master Drop Function
slug: master_drop_function
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_drop_function.htm
source: Advantage CHM
tags:
  - master
checksum: 2086ad090723b3c513b01fd50cf1e7d75dbac4e4
---

# Master Drop Function

DROP FUNCTION

DROP FUNCTION

Advantage SQL Engine

| DROP FUNCTION  Advantage SQL Engine |  |  |  |  |

Removes a function from the database.

Syntax

DROP FUNCTION [package\_name.]function\_name

 

package\_name ::= identifier

function\_name ::= identifier

 

Remark

The DROP FUNCTION statement is used to remove a function from the database.

To remove a function that is not owned by any package, the user must have the DROP permission over the function. To remove a function that is owned by a package, the user must have the ALTER permission over the package.

Example

DROP FUNCTION test1;

DROP FUNCTION TestPack.test1;

 

See Also

[ALTER FUNCTION](master_alter_function.md)

[CREATE FUNCTION](master_create_function.md)

[CREATE PACKAGE](master_create_package.md)

[DROP PACKAGE](master_drop_package.md)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.md)
