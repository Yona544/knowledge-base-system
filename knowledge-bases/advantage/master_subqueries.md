Subqueries




Advantage Database Server 12  

Subqueries

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Subqueries  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Subqueries Advantage SQL Engine master\_Subqueries Advantage SQL > SQL Performance > Subqueries / Dear Support Staff, |  |
| Subqueries  Advantage SQL Engine |  |  |  |  |

The Advantage SQL engine supports subqueries in the WHERE clause and the HAVING clause of SELECT statements, the WHERE clause of DELETE statements and the WHERE clause of UPDATE statements. If a subquery does not have any outer reference, that is, reference to a column that belongs to a table that is not part of the FROM clause of the subquery, the Advantage SQL engine will optimize the subquery by executing the subquery only once and store the result set of the subquery for all subsequent evaluations of the condition involving the subquery.

If a subquery has any outer reference, the subquery is called a correlated subquery. The query engine cannot optimize a correlated subquery because the result set of the subquery is dependent on column values in the parent query. For each row in the tables in the parent query, a correlated subquery must be executed to generate the result set that is used to evaluate the condition involving the subquery. This can be very expensive if the parent query contains many rows.

In general, any outer references in the WHERE clause, HAVING clause, and the SELECT values list of the subquery will cause the subquery to be unoptimized, with the exception of a subquery related to an EXISTS operator. Because the SELECT values of the subquery are not used for the EXISTS operator, an outer reference in the SELECT values of a subquery that is used in an EXISTS comparison will not affect the ability to optimize the subquery. Often times, an SQL statement that uses a correlated subquery may be re-formulated to use a non-correlated subquery for improved performance.

Examples of optimized subqueries:

// List each employee who is a manager

SELECT \* FROM Employees WHERE EmployeeID IN ( SELECT ManagerID FROM Employees )

// List names of all customers who have not made any transactions in the last 90 days

SELECT Name FROM Customers WHERE CustomerID NOT IN ( SELECT CustomerID FROM Sales WHERE TransactionDate > Current\_Date - 90 )

// List all employees whose current month's sales amount exceeds $20,000

SELECT \* FROM Employees WHERE EmployeeID IN ( SELECT EmployeeID FROM Sales WHERE MonthName( TransactionDate ) = MonthName( Current\_Date() ) GROUP BY EmployeeID HAVING Sum( TransactionAmount ) > 20000 )

Examples of subqueries that cannot be optimized:

// List all employees who have already met current month's sales quota. Note that the

// subquery is correlated because of the outer reference in the HAVING clause of the subquery

SELECT \* FROM Employees WHERE EmployeeID IN ( SELECT EmployeeID FROM Sales WHERE MonthName( TransactionDate ) = MonthName( Current\_Date() ) GROUP BY EmployeeID HAVING Sum( TransactionAmount ) > Employees.SalesQuota )

 

The above query may be re-formulated into the following optimized form for significant performance improvement (note that the subquery no longer uses an outer reference):

SELECT \* FROM Employees WHERE EmployeeID IN ( SELECT s.EmployeeID FROM Sales s INNER JOIN Employees e ON s.EmployeeID = e.EmployeeID WHERE MonthName( s.TransactionDate ) = MonthName( Current\_Date() ) GROUP BY s.EmployeeID, e.SalesQuota HAVING Sum( s.TransactionAmount ) > e.SalesQuota )

// List each employee who is a manager and who supervises some employees in offices

// other than his/her own office

SELECT \* FROM Employees a WHERE a.EmployeeID IN ( SELECT b.ManagerID FROM Employees b WHERE a.OfficeID <> b.OfficeID )