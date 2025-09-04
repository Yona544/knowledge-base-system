---
title: Master Declare
slug: master_declare
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_declare.htm
source: Advantage CHM
tags:
  - master
checksum: 6d032213b3887e3fb4130c40ff8d87b2cb4159bc
---

# Master Declare

DECLARE

DECLARE

Advantage SQL Engine

| DECLARE  Advantage SQL Engine |  |  |  |  |

The DECLARE statement is used to declare variables and cursors.

Syntax

DECLARE variable\_declaration | cursor\_declaration [, ];

 

variable\_declaration ::= variable\_name variable\_type

cursor\_declaration ::= cursor\_name CURSOR [ AS cursor\_statement ]

cursor\_statement ::= select\_statement | execute\_statement

Description

All variables used in the script must be declared at the beginning of the script using one or more DECLARE statements. The Advantage Query Engine will perform type checking on variables when they are used in assignments or expressions. All variables are initialized to NULL when declared.

A cursor is not accessible until it is opened using the [OPEN](master_open_close_fetch.md) statement. Once a cursor is open, the column values in the cursor can be accessed using the dot notation: cursorname.columnname.

Note If a cursor\_statement is a SELECT statement with aggregate expressions or algebraic expressions in the select list, and if the expression columns are not aliased, the expression columns will be unnamed columns in the cursor and their values will be inaccessible in the script. It is thus imperative to provide aliases for the expression columns in the select list.

Variable and cursor names are case insensitive and cannot be a [reserved keyword](master_reserved_keywords.md) or a quoted identifier.

Although the Advantage SQL Engine does not require variable names to be in any specific format, the special character '@' may be used as the first character of a variable name to avoid potential conflicts between column names and variable names in SQL statements. The following sample script will illustrate the problem:

DECLARE empid Integer;

empid = 1;

UPDATE employees SET ManagerID = empid WHERE branch = 'R&D';

The intention of the script is to change the manager for all R&D branch employees to employee number 1. However, if there is a column named 'empid' in the table, which is a very likely scenario, the usage of the "empid" in the SET clause will be ambiguous. It can reference either the 'empid' column in the table or the variable empid. In case of this type of ambiguity, the error code 2229, ambiguous reference, will be returned.

To avoid this type a problem, the variable names in the SQL scripts should be declared with '@' as the first character. When the SQL engine encounters a name that begins with the '@' character, it will attempt to resolve it into a variable reference. If the name can be resolved into a variable reference, there will be no addition attempt to check for conflict with a column name. In other words, the 2229 error will never occur when using variable names that begin with the '@' character. Using this approach, the sample script above could be written as:

DECLARE @empid Integer;

@empid = 1;

UPDATE employees SET ManagerID = @empid WHERE branch = 'R&D';

The variable\_type can be any [supported data type](master_supported_data_types_in_the_advantage_sql_engine.md) with the exception of the AUTOINC, MODTIME or ROWVERSION types. In addition, STRING is a valid type that can be used to declare variable length ANSI/OEM character data. A STRING type variable is different from a CHAR(n) or VARCHAR(n) type variable in the following aspects:

- When string data is assigned to a CHAR(n) variable, the resultant string is always n characters long. If the source string is longer, it is truncated to n characters. If the source string is shorter than the CHAR(n) variable, the resultant string is padded with spaces to a length of n.

- Similar to a VARCHAR variable, when character data is assigned to a STRING variable, no padding will be performed. However, unlike VARCHAR variables, STRING variables can grow to any length, limited only by the resources available on the machine. Character data assigned to a VARCHAR(n) variable is limited to the maximum declared precision n, and excessive data is truncated. The ability of the STRING variable to grow to unlimited length has one drawback - it may be impossible to predetermine the true maximum size of an algebraic expression with STRING variables, so when a string variable is to be stored in a cursor, a MEMO field type may be use in the cursor to store the string data instead of the more efficient field types such as ADS\_STRING or ADS\_VARCHARFOX used for CHAR(n) and VARCHAR(n) variables respectively.

Example

DECLARE strLocal String;

DECLARE iLocal Integer, jLocal Integer;

DECLARE cLocal Char(20), Cursor1 Cursor, Cursor2 Cursor AS SELECT \* FROM employees;

 

OPEN Cursor2;

WHILE FETCH Cursor2 DO

 iLocal = Cursor2.empid;

END WHILE;
