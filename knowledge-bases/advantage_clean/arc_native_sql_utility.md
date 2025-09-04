---
title: Arc Native Sql Utility
slug: arc_native_sql_utility
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_native_sql_utility.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 1096fd41e085d58aca86954c1e4b774a19bcef4d
---

# Arc Native Sql Utility

SQL Utility

SQL Utility

Advantage Data Architect

| SQL Utility  Advantage Data Architect |  |  |  |  |

The Advantage Data Architect SQL Utility provides a convenient way to write and test queries using the Advantage SQL engine. See [Advantage SQL Engine](master_advantage_sql_engine.md) for more information.

Following is a list of tasks that can be performed using the SQL Utility:

- [Executing a Query](arc_native_sql_utility.md#executing_query)

- [Verify Query Syntax](arc_native_sql_utility.md#verifyingstatesyntax)

- [Setting Query Options](arc_native_sql_utility.md#queryoptions)

- [Enabling Encryption](arc_native_sql_utility.md#encryption)

- [Using Transactions](arc_native_sql_utility.md#transactions)

- [Data Dictionary Links](arc_native_sql_utility.md#data_dictionary_links)

- [Using Parameters](arc_native_sql_utility.md#parameters)

- [Retrieving SQL Execution Plans](arc_native_sql_utility.md#retrieving_sql_execution_plans)

Executing a Query

After a connection has been made, enter an SQL statement(s) and execute by clicking the Execute SQL button on the toolbar, or by hitting Alt-E on your keyboard. The execution of a query can be canceled by clicking the Cancel SQL button on the toolbar. If an SQL query takes more than 2 seconds to complete, the progress of the execution of that query will be displayed in a progress bar above the grid.

Query Scripts

To save an existing query to an SQL script file, click the Save button on the toolbar. To load an existing script file, click the Open button on the toolbar.

An SQL script consists of one or more statements separated by semicolons. If you want to execute only one or two statements in the script, select the statements to execute by dragging your mouse over them (or using the shift | arrow key combination) and click the Execute SQL button.

If a script is executed, and the final statement in the script does not return a result set, no result set will be shown. Only the success or error message will be returned.

If a script ends in a statement that returns a result set, that result set will be displayed in the grid.

For more information on SQL scripts, see [Scripts](master_sql_script_overview.md).

Verifying Statement Syntax

The Verify button can be used to verify the syntax of the current statement without actually executing the statement. This functionality is useful when working with a time consuming SQL statement.

Query Options

Query options can be configured by going to the ARC Settings menu item under the main Tools menu. Select the Query tab to view and/or modify query options

- Column display sizes

- Script file behavior

Encryption

If running SQL queries on a free table(s)) that has been encrypted, the encryption password for that table(s) can be specified via the Table Encryption Password(s) option in the SQL menu on the main menu bar. A more convenient but less secure method of providing the passwords is to use the ExtraConnectString property in the connection repository.  You could specify them to be provided as part of the connection string that way.  For example, "EncryptionPassword=table1=password1,table2=password2;".  This is not a secure mechanism, though, because the information is persisted to the ads.ini file without any encryption. Thus, anyone with access to the machine could view the passwords.

Transactions

Once a successful connection has been made to the Advantage Database Server (i.e., a remote connection), the ability to run SQL queries inside a transaction exists. The Begin Transaction, Commit Transaction, and Rollback Transaction options control the transaction processing functionality.

Data Dictionary Links

The Link Manager option on the main SQL menu opens the SQL Link Manager, which is used to create temporary data dictionary links.

Parameters

Named parameters (such as :myparam) are supported by the SQL Utility. Unnamed parameters (such as ?) are not currently supported. To use parameter support, simply execute a statement that has named parameters. A parameter dialog box will appear asking for the parameter data type and value. An example statement with a parameter is shown below:

select \* from demo10 where lastname = :last

Re-execute the query and the parameter dialog will reappear, allowing you to enter new parameter values for the next query execution.

Retrieving SQL Execution Plans

The Show Plan button can used to retrieve a graphical representation containing information about how the Advantage Query Engine will execute a query. The graphical representation of the query execution plan is shown on the [SQL Execution Plan](master_sql_execution_plan.md) tab sheet. The static cursor containing the execution plan returned from the server is displayed on the Data tab sheet. More information about the static cursor returned for the server can be found [here](master_sql_execution_plan.md).

Each execution plan is composed of series of icons representing server operations connected by arrows showing the flow of data from one operation to another. The top left hand node of a plan for a query contains the statement to be executed. All other nodes signify an operation of required to complete that query. All SQL statements are verified for correctness before a plan is displayed.

Hovering over the icon of an operation with the mouse will display a pop-window containing more information about the operation. This always includes:

- The type of operation.

- A description of the operation.

The pop-up windows can also contain:

- The estimated number of times the operation will be executed.

- Any arguments to the operation.

- Detailed warnings if an operation cannot be optimized.

Any operation displaying a red circle is not optimized and should be investigated to prevent poor performance. Many times the operation could not be optimized because an appropriate index was not available for the Advantage Query Engine to use.

To create an index on a table, simply right click on the Table Scan icon and select Create Indexes. This will display the Index Management Utility with information about the current table. When the Index Management Utility is closed the execution plan will be retrieved again, so the most current information is displayed.

The following icons are displayed in the graphical representation:

| Icon | Operation |
|  | [DELETE](master_delete_sql_execution_plan.md) |
|  | [DISTINCT](master_distinct.md) |
|  | [EVALUATE](master_evaluate.md) |
|  | [GROUP BY](master_group_by.md) |
|  | [INDEX SCAN](master_index_scan.md) |
|  | [INSERT INTO](master_insert_into.md) |
|  | [JOIN/LEFT OUTER JOIN](master_join_left_outer_join.md) |
|  | [SORT](master_sort.md) |
|  | [TABLE SCAN](master_table_scan.md) |
|  | [UNION ALL](master_union_all.md) |
|  | [UPDATE](master_update_sql_execution_plan.md) |
