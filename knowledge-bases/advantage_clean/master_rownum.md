---
title: Master Rownum
slug: master_rownum
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_rownum.htm
source: Advantage CHM
tags:
  - master
checksum: 954f7101ffee5d6643a99591c795b4a987b8ad63
---

# Master Rownum

ROWNUM

ROWNUM

Advantage SQL Engine

| ROWNUM  Advantage SQL Engine |  |  |  |  |

The scalar function ROWNUM() can be used to generate numbers starting at 1 for each row in the result of a query.  The ROWNUM() function is primarily intended for use in the select list.

ROWNUM() can be used in a select list to provide a numbering of the rows in the result set. The number associated with a row is determined when the row is selected for inclusion in the result set.  In the following query the number of the first row of the result set will be determined by how the query is optimized:

SELECT ROWNUM(), Lastname FROM employees ORDER BY LASTNAME

If an existing index is used to populate the result set the first row will be numbered 1.  If the query can be more efficiently optimized by sorting the rows after adding them to the result the row number will be determined when the base record is found in the table.

Testing if a value returned by ROWNUM() is greater than a positive integer will always return false. The following query is always empty:

SELECT \* FROM employees WHERE ROWNUM() > 1

Each row fetched is assigned the number 1, but that does not satisfy the condition.  Because no rows are added to the result set the number is never incremented.

The preferred method for performing Top-N reporting or limiting rows in a result set is to use the [TOP X](master_select.md) syntax.

See Also

[SELECT](master_select.md)

[ROWID](master_rowid.md)

[Supported Scalar Functions](master_supported_scalar_functions.md)
