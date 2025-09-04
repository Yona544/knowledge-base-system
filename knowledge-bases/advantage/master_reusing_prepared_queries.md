Reusing Prepared Queries




Advantage Database Server 12  

Reusing Prepared Queries

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Reusing Prepared Queries  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Reusing Prepared Queries Advantage SQL Engine master\_Reusing\_prepared\_queries Advantage SQL > SQL Performance > Reusing Prepared Queries / Dear Support Staff, |  |
| Reusing Prepared Queries  Advantage SQL Engine |  |  |  |  |

Reusing prepared queries will increase performance because the SQL command does not have to be parsed again. Prepared queries are invalidated when the statement handle is freed.

Using prepared SQL statements can increase performance. When an application executes an SQL statement, the Advantage SQL engine parses the statement and creates an execution plan with optimization information and initializes the tables that are referenced by the SQL statement. It is possible to prepare a statement and execute it multiple times. This allows Advantage to skip the parsing and optimization with all but the first execution of the statement. With each execution, the client sends the updated parameters to the server, which can then immediately execute the statement.

A simple example of a statement that might be prepared and reused is:

UPDATE employee SET salary = salary \* ? WHERE empid = ?

The two parameters (represented with the ? character) can be updated to different values with each execution of the statement. The mechanism to use prepared queries and to assign parameter values depends on the development environment. If you are using the Advantage Client Engine API directly, see AdsPrepareSQL for more information. When using the TDataSet Descendent, use the Prepare method and the Params property. With ADO, an application can use the Command objects Prepared property and CreateParameter method.