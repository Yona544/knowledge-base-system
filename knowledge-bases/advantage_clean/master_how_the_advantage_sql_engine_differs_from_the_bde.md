---
title: Master How The Advantage Sql Engine Differs From The Bde
slug: master_how_the_advantage_sql_engine_differs_from_the_bde
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_how_the_advantage_sql_engine_differs_from_the_bde.htm
source: Advantage CHM
tags:
  - master
checksum: f684c09c5ddf2357bc53eb7deab2f9d840b93183
---

# Master How The Advantage Sql Engine Differs From The Bde

How the Advantage SQL Engine Differs from the BDE

How the Advantage SQL Engine Differs from the BDE

Advantage SQL Engine

| How the Advantage SQL Engine Differs from the BDE  Advantage SQL Engine |  |  |  |  |

The following table shows how the Advantage SQL engine differs from Borland Database Engine (BDE) Local SQL.

| SQL Construct | BDE Local SQL | Advantage SQL Engine |
| Concatenation Operator | Supported by the "||" operator. Strings are automatically trimmed. | Supported by the "+" operator. Strings are not automatically trimmed. |
| SOME keyword | Supported | Not Supported |
| FROM | Support BDE alias in the FROM clause. For example: FROM ":DBDemos:Orders". | Does not support database alias in the FROM clause. |
| ORDER BY | Support ORDER BY using ASCENDING/DESCENDING keywords. | Support ORDER BY using ASC/DESC keywords. |
| Quoted Strings | Supports single and double quotes interchangeably. | Single quotes are used for character string literals. Double quotes and square brackets are used for delimiting table and field names. |
| Comparison to NULL | "field = NULL" is supported. | Supported through the standard syntax "field IS NULL". |
| Not Equal Comparison | Supports "!=" operator | Does not support "!=" operator. Only "<>" operator is supported. |
| Named parameter | Any character except white spaces. | If the name is not quoted with ", only characters A-Za-z and \_ is allowed in the name. If other character is to appear in the parameter name, the name must be quoted with ". For example, :"Last+First" |
| Numeric value | Can be enclosed in quotes. For example: IntField = '2' or IntField = 3 | Must not be enclosed in quotes. For example:  IntField = 2 or IntField = 3 |
