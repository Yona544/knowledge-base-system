---
title: Master Delete
slug: master_delete
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_delete.htm
source: Advantage CHM
tags:
  - master
checksum: 8bd86765b2427349afdb8e47a101ceb0fbfa523f
---

# Master Delete

DELETE

DELETE

Advantage SQL Engine

| DELETE  Advantage SQL Engine |  |  |  |  |

Deletes a record from a table in the database

Syntax

DELETE FROM <table-name> [WHERE <search-condition>]

search-condition ::= expression with a logical result

Remarks

Comparison is a valid predicate expression; can also include a dynamic parameter.

Positioned deletes not supported.

The {ts/d/t} format is not required in the search condition for timestamp, date, or time values.

If the DELETE statement is executed on a database connection) and the database has been set up to verify the user access rights, to successful execute the query, the user must have WRITE rights to the table.

When deleting multiple records, the SQL engine gets record locks as it performs the deletes. It makes several attempts to get a record lock. If it fails to get the lock, it continues on and attempts to complete the rest of the delete operations. If this happens, the error (5035) is returned to the client, which must then assume that one or more record deletes failed to occur. If an application requires all the deletes to occur as an atomic operation, it should issue the DELETE statement in a transaction.

Example(s)

DELETE FROM customer WHERE purch\_amt < 100.00 AND NOT state = CA

DELETE FROM customer WHERE purch\_date < {d 1980-07-31}

DELETE FROM customer WHERE purch\_date < 1980-07-31

DELETE FROM customer WHERE customer.id NOT IN

(SELECT custid FROM orders WHERE orders.custid = customer.id )
