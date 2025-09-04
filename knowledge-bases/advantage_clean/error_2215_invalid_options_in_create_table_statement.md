---
title: Error 2215 Invalid Options In Create Table Statement
slug: error_2215_invalid_options_in_create_table_statement
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2215_invalid_options_in_create_table_statement.htm
source: Advantage CHM
tags:
  - error
checksum: eba18568edf47c1e18025602084a2945c9543643
---

# Error 2215 Invalid Options In Create Table Statement

2215 Invalid options in CREATE TABLE statement

2215 Invalid options in CREATE statement

Advantage Error Guide

| 2215 Invalid options in CREATE statement  Advantage Error Guide |  |  |  |  |

An invalid option is specified in the CREATE statement. The error text should contain more information about the specific error. For example: the following CREATE TABLE statement returns the error because it specified both options to create a temporary table and a database table.

CREATE TABLE #Table1 ( id integer, name char(20) ) IN DATABASE

The # prefix before the table name specifies that the table is a temporary table while the IN DATABASE clause specifies that the table should be added into the data dictionary. An error is returned because the two options are mutually exclusive.

The error may also be returned when invalid options are specified in a CREATE INDEX, a CREATE FUNCTION, a CREATE PACKAGE statement or other CREATE statement.
