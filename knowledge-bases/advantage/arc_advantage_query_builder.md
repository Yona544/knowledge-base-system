Advantage Query Builder




Advantage Database Server 12  

Advantage Query Builder

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Query Builder  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Advantage Query Builder Advantage Data Architect arc\_Advantage\_query\_builder Advantage Data Architect > Using SQL with Advantage Data Architect > Advantage Query Builder / Dear Support Staff, |  |
| Advantage Query Builder  Advantage Data Architect |  |  |  |  |

The Advantage Query Builder provides a graphical interface for building SQL queries.

Before a query can be built, you must connect to a database. See Connection Repository for details on making a connection.

To build a query:

|  |  |
| --- | --- |
| 1. | Choose the table or tables you want to query by dragging them to the modeling work area. |

|  |  |
| --- | --- |
| 2. | If you wish to create a multi-table query, link the tables you have selected by dragging a field from one table to the corresponding field of another table. |

|  |  |
| --- | --- |
| 3. | Select the fields you want displayed in the result by clicking to the left of the desired fields in each table object. |

|  |  |
| --- | --- |
| 4. | Specify an ORDER BY clause by right clicking the box in the Sort row for the desired column and selecting Ascending or Descending (optional). |

|  |  |
| --- | --- |
| 5. | Specify aggregate functions to perform on the data by right clicking the box in the Function row for the desired column (optional). |

|  |  |
| --- | --- |
| 6. | Specify a GROUP BY clause by right clicking the box in the Group row for the desired column and selecting Group (optional). |

|  |  |
| --- | --- |
| 7. | Generate the SQL statement syntax by clicking Generate SQL. The SQL syntax will be displayed in the SQL tab window. |

|  |  |
| --- | --- |
| 8. | Execute the query by clicking Run Current SQL. The result set of the query will be displayed in the Results tab window. |

Clicking the Save SQL option can save the query. The result of a successful query can be saved to a table by clicking Save Results. Clicking the Save Model option can save the SQL query model. A previously saved query model can be re-opened by clicking Open Model.

All tables inside a join or simple select statement are given a unique alias for use inside of the query. The alias is the first letter of the name of the table. If two or more table names starting with the same character exist, a number is concatenated to the first letter of the table.

The Advantage Query Builder can be used to create SQL queries containing both inner and left outer joins. The order of tables in the join is very important and determines how the join operator is applied. The resulting syntax of an inner join is:

Table1.Column Operator Table2.Column

For an outer join, the order of the tables is even more important because it determines which table will have NULL-extended copies of the unmatched rows. For the Advantage Query Builder, table 1 will have the NULL-extended rows. The resulting syntax of a left outer join is:

Table1 LEFT OUTER JOIN Table2 ON Table1.Column Operator Table2.Column