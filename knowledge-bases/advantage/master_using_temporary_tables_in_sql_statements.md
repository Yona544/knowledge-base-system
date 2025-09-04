Using Temporary Tables in SQL Statements




Advantage Database Server 12  

Using Temporary Tables in SQL Statements

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Temporary Tables in SQL Statements  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using Temporary Tables in SQL Statements Advantage SQL Engine master\_Using\_temporary\_tables\_in\_sql\_statements Advantage SQL > SQL Functionality > Using Temporary Tables in SQL Statements / Dear Support Staff, |  |
| Using Temporary Tables in SQL Statements  Advantage SQL Engine |  |  |  |  |

[Temporary tables](master_temporary_tables.htm) can be used in the SQL statement wherever the regular tables can be used. To identify a table being a temporary table in the SQL statement, prefix the table name with the # character.

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