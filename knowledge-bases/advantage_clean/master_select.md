---
title: Master Select
slug: master_select
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_select.htm
source: Advantage CHM
tags:
  - master
checksum: e7afbdfd4ab373f29a35f27d6664e58710947516
---

# Master Select

SELECT

SELECT

Advantage SQL Engine

| SELECT  Advantage SQL Engine |  |  |  |  |

Retrieves data from the database.

 

Syntax

SELECT <select-spec> [<select-order-by>]

or

SELECT <select-spec> UNION [ALL] <select-spec> [ UNION [ALL] <select-spec> ] [<union-order-by>]

or

SELECT <top> <select-spec> [<select-order-by>]

top ::= TOP {integer} [START AT integer] | TOP {integer} PERCENT

select-spec ::= [{static}] [ALL | DISTINCT] <select-list> [INTO tablename] FROM <table-reference-list>

[WHERE <search-condition>]

[GROUP BY <grouping-column> [, < grouping-column]]

[HAVING <search-condition>]

select-order-by ::= ORDER BY {<column-name> | integer} [ASC | DESC][,

{<column-name> | integer}[ ASC | DESC ]]

union-order-by ::= ORDER BY {integer} [ASC|DESC][,

{integer}[ ASC | DESC ]]

table-reference-list ::= table-list-item , table-reference-list | table-list-item

table-list-item ::= table-ref |inner join | outer-join | { OJ outer-join }

inner-join = table-ref INNER JOIN table-ref ON boolean | inner-join INNER JOIN table-ref ON boolean

outer-join ::=  table-ref LEFT [OUTER] JOIN table-ref ON boolean |

 table-ref LEFT [OUTER] JOIN outer-join ON boolean | outer-join LEFT [OUTER]    JOIN table-ref ON boolean |

table-ref RIGHT [OUTER] JOIN table-ref ON boolean |

table-ref RIGHT [OUTER] JOIN outer-join ON boolean | outer-join RIGHT [OUTER] JOIN table-ref ON boolean |

table-ref FULL [OUTER] JOIN table-ref ON boolean |

table-ref FULL [OUTER] JOIN outer-join ON boolean | outer-join FULL [OUTER] JOIN table-ref ON boolean

table-ref ::= table-name | table-name alias-name | execute-procedure alias-name

search-condition ::= expression with a logical result

 

Remarks

The optional escape sequence {static} may be used in the SELECT statement to force a static cursor. See [Cursor Types](master_cursor_types.md) for a description of live and static cursors.

The optional [INTO tablename] clause can only be specified once in the statement and it must appear in the first SELECT in the SQL statement. It cannot be used in subquery. When the INTO clause is specified, the result set will be stored in the specified table and a live cursor will be returned. The new table is fully populated before the control is returned back to the client. The newly created table will be always be a free table even when the statement is executed on a database connection) and the user executing the statement has the permission to create table in the database.

If the SELECT statement is executed on a database connection) and the database has been set up to verify the user access rights, to successful execute the query, the user must have READ rights to all table(s) and view(s) in the FROM clause of the statement.

In Advantage StreamlineSQL, the GROUP BY clause and the ORDER BY clause can be a combination of expression, column name, column alias or column ordinal. The followings are all valid statements in Advantage:

-- GROUP BY using expression and ORDER BY using column ordinal

SELECT lastname + firstname AS fullname, count(\*)

FROM emp

GROUP BY lastname + firstname

ORDER BY 2 DESC

 

-- GROUP BY using alias and ORDER BY using alias

SELECT lastname + firstname AS fullname, count(\*) AS cnt

FROM emp

GROUP BY fullname

ORDER BY cnt DESC

 

-- GROUP BY using column ordinal and ORDER BY using column ordinal

SELECT lastname + firstname AS fullname, count(\*) AS cnt

FROM emp

GROUP BY 1

ORDER BY 2 DESC

 

-- GROUP BY using column names and ORDER BY using column ordinal

SELECT lastname + firstname AS fullname, count(\*) AS cnt

FROM emp

GROUP BY lastname, firstname

ORDER BY 2 DESC

 

If there is an ambiguity on whether a GROUP BY column or a ORDER BY column is a base column name or a column alias, Advantage will resolve the GROUP BY column into the column alias. For example, the following sample statements are equivalent:

SELECT IIF( lastname IS NULL, '', lastname ) AS lastname, count(\*) AS cnt

FROM emp

GROUP BY lastname;

 

SELECT IIF( lastname IS NULL, '', lastname ) AS lastname, count(\*) AS cnt

FROM emp

GROUP BY IIF( lastname IS NULL, '', lastname );

 

This should be kept in mind when an result column is aliased to be the same as a base column name. This following statement will not execute in Advantage:

SELECT IIF( lastname IS NULL, '', lastname ) AS lastname,

IIF( lastname = 'Coles', 'Stand out', 'Average' ) As Type,

count(\*) AS cnt

FROM emp

GROUP BY lastname;

 

The "lastname" in the GROUP BY clause will be resolved into the alias referencing the first IIF expression, leaving the "lastname" column in the second IIF expression as a column that is not part of the GROUP BY clause, a construction not allowed by the ANSI SQL standard. To make sure the GROUP BY clause referring to the column in a base table, use the table.column notation. The above example can be alter to be an valid SQL statement as shown below:

SELECT IIF( lastname IS NULL, '', lastname ) AS lastname,

IIF( lastname = 'Coles', 'Stand out', 'Average' ) As Type,

count(\*) AS cnt

FROM emp

GROUP BY emp.lastname;

 

The TOP clause allows a query to select a subset of records in a result set. The TOP value must be greater than or equal to 0.  The offset value must be greater than 0.  See [Limiting Query Results](master_limiting_query_results.md) for details.

To perform full text searches, use the CONTAINS() scalar function in the SELECT statement. Advantage provides a powerful full text search engine that can search character fields as well as memos and BLOBs for given words and phrases. See [Full Text Search](master_full_text_search.md) for details.

The UNION syntax provides the capability to combine two or more SELECT statement results together into a single result set. By default, duplicate rows are eliminated from the result set (similar to DISTINCT). If the ALL keyword is provided, then all rows are returned in the result set (duplicate rows are not removed).

Statements used in a UNION can only have ORDER BY clauses on the last statement of the UNION. If an ORDER BY clause is placed at the end of a UNION statement, the ORDER BY would apply to the result of the entire UNION, not just the last statement in the UNION. If a statement within the UNION must have an ORDER BY clause, the statement can be turned into a subquery, which then can have the ORDER BY.

For example, this statement is allowed:

SELECT empid, fullname FROM branch1 UNION SELECT empid, fullname FROM branch2 ORDER BY empid

This statement is NOT allowed:

SELECT TOP 10 empid, fullname FROM branch1 ORDER BY empid UNION SELECT empid, fullname FROM branch2 ORDER BY empid

 

To get the desired result of the statement above, it can be modified like this:

SELECT \* FROM (SELECT TOP 10 empid, fullname FROM branch1 ORDER BY empid) a UNION SELECT empid, fullname FROM branch2 ORDER BY empid

 

 

Example(s)

 

SELECT \* FROM emp

 

SELECT DISTINCT lastname, firstname, idname FROM emp

 

SELECT \* FROM emp WHERE lastname = 'Smith'

 

SELECT salesrep FROM sales GROUP BY emp\_id HAVING sales > 10000

 

SELECT \* FROM sal ORDER BY emp\_id

 

SELECT \* FROM emp WHERE hire\_date < '1992-02-22'

 

SELECT \* FROM emp WHERE hire\_date < {d '1992-02-22'}

 

SELECT \* FROM emp WHERE hire\_date > '1993-01-31' AND hire\_date < {d '1993-01-31'} + 30

 

SELECT \* FROM emp WHERE hire\_date - quit\_date > 30 ORDER BY lastname

 

SELECT \* FROM emp LEFT OUTER JOIN sal ON emp.emp\_id = sal.emp\_id

 

SELECT \* FROM emp WHERE emp.emp\_id IN (SELECT sal.emp\_id FROM sal WHERE sal.dept <> HR )

 

SELECT \* FROM oldcust WHERE oldcust.sales > 50000 UNION ALL

 

SELECT \* FROM newcust WHERE newcust.sales > 50000

 

SELECT emp.lastname, sal.salary, dept.deptname FROM emp LEFT OUTER JOIN sal ON emp.emp\_id = sal.emp\_id, dept WHERE emp.dept\_id=dept.dept\_id

 

SELECT emp.lastname, sal.salary, dept.deptname

 INTO lastname\_sal

 FROM emp LEFT OUTER JOIN sal ON emp.emp\_id = sal.emp\_id,

 WHERE emp.dept\_id=dept.dept\_id

 

SELECT TOP 100 \* FROM emp

 

SELECT TOP 15 PERCENT lastname, firstname, idname FROM emp

 

SELECT TOP 10 DISTINCT lastname, firstname, idname FROM emp

Perform a full text search and order the result set with the records that have the most hits at the top. For full details, see [Full Text Search](master_full_text_search.md)

SELECT \* FROM applicants WHERE CONTAINS( interests, 'skiing and "mountain climbing" ' )

ORDER BY SCORE( 1 ) DESC

Use the results of a stored procedure in the FROM clause:

SELECT \* FROM (EXECUTE PROCEDURE TopCustomers( 1, '2010-02-28' )) proc\_results WHERE total\_sales > 10000
