Temporary Tables




Advantage Database Server 12  

Temporary Tables

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Temporary Tables  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Temporary Tables Advantage Concepts master\_Temporary\_tables Advantage Concepts > Advantage Functionality > Temporary Tables / Dear Support Staff, |  |
| Temporary Tables  Advantage Concepts |  |  |  |  |

Advantage Database Server and Advantage Local Server support the creation and utilization of temporary tables that are local to each user connection. To identify a temporary table, prefix the name with a hash character (#). Thus, if you create a table named "#mytable", it will be a temporary table.

Temporary tables are otherwise identical to regular tables except for two unique properties that make them ideal for storing temporary or intermediate data for complex transactions. First, temporary tables are visible only on the connection where the temporary tables are created. This eliminates the possibility of name conflict when creating a temporary table. There could be multiple temporary tables named "#Temp1" residing on different connections. Secondly, temporary tables are automatically deleted when the connection that creates them is closed. In other words, the scope of the temporary table is the current connection. This removes responsibility of maintaining the temporary table from the application. The Advantage Database Server or Advantage Local Server is responsible for creating the temporary table and removing them when they are out of scope. The application may still explicitly remove the used temporary tables to reduce the resource usage on the server.

Temporary tables can be used on both the [free connection](javascript:hhpopuplink.TextPopup(popid_1658562324,FontFace,-1,-1,-1,-1)) and the [database connection](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)). Advantage may create a physical table with a unique name to represent each temporary table. Where the physical files are located is dependant on the server type and the connection type. With Advantage Local Server, the temporary files are always created on the local computer and located in the Windows temporary directory for the current user. With Advantage Database Server, the location of the file depends on the whether the connection is a [free connection](javascript:hhpopuplink.TextPopup(popid_1658562324,FontFace,-1,-1,-1,-1)) or a [database connection](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)). With a [free connection](javascript:hhpopuplink.TextPopup(popid_1658562324,FontFace,-1,-1,-1,-1)), the temporary files are located in the same directory as the connection path. With a [database connection](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)), the files are located in the temporary directory specified in the data dictionary.

Advantage fully caches temporary tables in memory when possible. Only when Advantage cannot fit temporary table data in its cache (or when it is configured to not cache any data) will it create a physical file for temporary tables or write table data to disk.

Temporary tables can be [created and used in SQL statements](master_using_temporary_tables_in_sql_statements.htm) and with APIs such as [AdsCreateTable90](ace_adscreatetable.htm) and [AdsOpenTable90](ace_adsopentable90.htm) API. Temporary tables created with SQL can be accessed through the APIs and vice versa.

See Also

[Using Temporary Tables in SQL Statements](master_using_temporary_tables_in_sql_statements.htm)