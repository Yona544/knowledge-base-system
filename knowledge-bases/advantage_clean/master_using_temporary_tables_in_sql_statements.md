---
title: Master Using Temporary Tables In Sql Statements
slug: master_using_temporary_tables_in_sql_statements
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_using_temporary_tables_in_sql_statements.htm
source: Advantage CHM
tags:
  - master
checksum: 8220cb12aff14998d543a3b604dd246d1214efea
---

# Master Using Temporary Tables In Sql Statements

Using Temporary Tables in SQL Statements

Using Temporary Tables in SQL Statements

Advantage SQL Engine

| Using Temporary Tables in SQL Statements  Advantage SQL Engine |  |  |  |  |

[Temporary tables](master_temporary_tables.md) can be used in the SQL statement wherever the regular tables can be used. To identify a table being a temporary table in the SQL statement, prefix the table name with the # character.

Examples:

// Create a temporary table named Temp1 with two columns

 

CREATE TABLE #Temp1 ( Name Char( 30 ), seqid integer );

 

 

 

// This example creates two temporary tables for intermediate results

// Step 1. Create a temporary table named DeptCount and at the same time

// populate it with summary data from an existing table in the

// database

 

SELECT deptnum, count(\*) as NumEmployees

INTO #DeptCount

FROM employees

GROUP BY deptnum

 

// Step 2. Create another temporary table named LocCount which list the

// number of employees in each location for each department.

 

SELECT deptnum, location, count(\*) as cnt

INTO #LocCount

FROM employees

GROUP BY deptnum, location

 

// Finally using the 2 temporary tables to list the percent of employee

// on each location for each department

 

SELECT a.deptnum, a.location, ( a.cnt \* 100 ) / b.NumEmployees As PercentAtLocation

FROM #LocCount a, #DeptCount b

WHERE a.deptnum = b.deptnum
