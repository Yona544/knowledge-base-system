---
title: Master User Defined Function
slug: master_user_defined_function
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_user_defined_function.htm
source: Advantage CHM
tags:
  - master
checksum: ce8f9fde06686ce92e9f693ef7a539fd83c8a830
---

# Master User Defined Function

USER DEFINED FUNCTION

USER DEFINED FUNCTION

Advantage SQL Engine

| USER DEFINED FUNCTION  Advantage SQL Engine |  |  |  |  |

User Defined Functions (UDFs) allow a developer to create reusable functions that can be used in an SQL statement or SQL script just like existing system scalar functions. By encapsulating frequently performed or complex operations into user defined functions, SQL statements or scripts become easier to write, understand, and debug. In a sense, UDFs make it possible to extend the functionality of the SQL engine.

UDFs also make it simpler for developers to alter the behavior of their application without recompiling. For example, different countries in the world have different formats for displaying monetary data. Instead of creating separate versions of SQL statements for each country, the developer can have one version of the SQL statement that utilizes a UDF to perform the transformation of the monetary data into character format. By either making the UDF return different character strings based on an environment variable or deploying different implementations of the same UDF to different countries, the application can present the monetary data in the correct format.

Advantage Database Server supports the concept of Function Packages to provide independent name spaces for the functions. This allows developers to deploy UDFs into an existing database without worrying about name conflicts.

See Also

[ALTER FUNCTION](master_alter_function.md)

[CREATE FUNCTION](master_create_function.md)

[CREATE PACKAGE](master_create_package.md)

[DROP FUNCTION](master_drop_function.md)

[DROP PACKAGE](master_drop_package.md)
