AXSQL Parameter Support




Advantage Database Server 12  

AXSQL Parameter Support

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AXSQL Parameter Support  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - AXSQL Parameter Support Advantage AXSQL RDDs Vo\_Axsql\_parameters Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > AXSQL Parameter Support / Dear Support Staff, |  |
| AXSQL Parameter Support  Advantage AXSQL RDDs |  |  |  |  |

The AdsSQLServer class supports SQL parameters in the constructor (init) and [Refresh](vo_axsql_refresh_functionality.htm) methods.  Read more about parameters in SQL statements [here](devguide_parameters_in_sql_statements.htm) and [here](ace_parameters_in_sql_statements.htm).  Parameters in VO are passed in using key-value arrays.  The first argument is the parameter name (key) and the second argument is the parameter value.  For example:

{{ "Lastname", "Smith" }}

Multiple parameters can be passed in like so:

{{"Lastname", "Smith"}, {"CustomerID", 100 }}

The AdsSQLServer class supports both named and unnamed parameters.  Unnamed parameters are placed in the SQL query using a question mark (?) and then set using numbers based on their position in the query.  For example:

oServer := AdsSQLServer{ "SELECT \* FROM customers WHERE Lastname = ? and Firstname = ?", , , "AXSQLADT", , {{ 1, "Coles" }, {2, "Becky" }}}

or

oServer:Refresh({{ 1, "Coles" }, {2, "Jenny" }} )