---
title: Master Case Insensitive Field Type
slug: master_case_insensitive_field_type
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_case_insensitive_field_type.htm
source: Advantage CHM
tags:
  - master
checksum: c6aec5191cfcdd92384fc5176dc7afb32e077418
---

# Master Case Insensitive Field Type

Case Insensitive Field Type

Case Insensitive Field Type

Advantage Concepts

| Case Insensitive Field Type  Advantage Concepts |  |  |  |  |

The case insensitive field type can be used when you do not want the case of character data to affect filter expressions, SQL WHERE clauses, index seeks, scalar functions, xbase expression engine functions, etc.

The case insensitive field type is called CICHAR when used via SQL, and cicharacter when used with ARC or from ACE calls such as AdsCreateTable.

Consider the following example. If you have a table with the following structure:

| csfield | character | 30 |
| cifield | cicharacter | 30 |

and the following data:

| csfield | cifield |
| hello | hello |
| Hello | Hello |
| HELLO | HELLO |

A filter of "csfield = hello" and the SQL statement "SELECT \* FROM table WHERE csfield = hello" would both return the following result set:

| hello | hello |

However, if you use the case insensitive column and a filter of "cifield = hello" or the SQL statement "SELECT \* FROM table WHERE cifield = hello" you would get the following result set:

| hello | hello |
| Hello | Hello |
| HELLO | HELLO |

Case insensitive fields also affect the behavior of scalar functions and expression engine functions that operate on string values. For example, if using the example dataset from above

SELECT POSITION( lo in cifield ) FROM table

will return a different result set than

SELECT POSITION( lo in csfield ) FROM table

Comparison Operators and Coercion

Comparison operators (such as =, <, >, etc) are also affected by the case sensitivity of a field (as we saw in the first example).

Comparison operators use a fields collation language and its coercion type to determine if the comparison is legal. A quick definition of each of these terms will be necessary before discussing what comparisons are legal and what comparisons are not legal.

Advantage currently supports two column-level collation languages (Note: we are discussing column-level collation languages, Advantage supports many different collation languages at the server level).

ads\_default\_cs  column-level collation language assigned to case sensitive fields

ads\_default\_ci  column-level collation language assigned to case insensitive fields

At first glance, this would mean in the following comparison

cifield = csfield

the comparison operator (=) would not know how to compare the values. Should it do a case insensitive comparison or a case sensitive comparison?

This is where coercion types enter the picture. Advantage uses 4 different coercion types.

| COERCION\_EXPLICIT | Assigned when a value is explicitly coerced using the COLLATE function or COLLATE clause (in SQL) |
| COERCION\_IMPLICIT | Assigned to column references |
| COERCION\_COMPATIBLE | Assigned to string literals |
| COERCION\_NECESSARY | Assigned to a value that is the result of a function that did not take any string input parameters but returned a string |

Coercion types have precedence: COERCION\_EXPLICIT takes precedence over COERCION\_IMPLICIT that takes precedence over COERCION\_COMPATIBLE.

When comparing two operands they must have the same collation language. If they dont, one operand must have a higher coercion type than the other. The collation language of the operand with the highest precedence coercion type will be used to perform the comparison operation.

In the example above (cifield = csfield) both operands have a coercion type of COERCION\_IMPLICIT, but have different collation languages. This comparison is illegal. To correct the expression, one side must be explicitly coerced.

Filter Expression:

cifield = collate( csfield, ads\_default\_ci )

SQL Expression:

cifield = csfield COLLATE ads\_default\_ci

The examples above modify the right side operand to have a coercion type of COERCION\_EXPLICIT, forcing a case insensitive comparison of the two operands.

Explicit coercions can be helpful if you have one case insensitive field that you often compare with other case sensitive fields, but you do not want to convert the other fields to be case insensitive as well.

Explicit coercions can also be used to change the case sensitivity of an operator even when case insensitive fields are not being used. It is often necessary to filter a dataset using a case insensitive search. The following two SQL expressions are equivalent:

UPPER( csfield ) = SEARCHSTRING

csfield = SEARCHSTRING COLLATE ads\_default\_ci

Note Comparisons performed by the Advantage expression engine and the Advantage query engine will be case insensitive comparisons. Comparisons performed in any client development environment will not, unless you use a case insensitive comparison function in that environment.
