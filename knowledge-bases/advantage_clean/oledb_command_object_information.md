---
title: Oledb Command Object Information
slug: oledb_command_object_information
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_command_object_information.htm
source: Advantage CHM
tags:
  - oledb
checksum: 982f3ea1415f299a9bd9d754c679ef36a9cff847
---

# Oledb Command Object Information

Command Object Information

Command Object Information

Advantage OLE DB Provider (for ADO)

| Command Object Information  Advantage OLE DB Provider (for ADO) |  |  |  |  |

Advantage SQL support consists of most of the SQL-92 standard with ODBC extensions. See [Supported SQL Statements](master_supported_sql_statements.md) for detailed information on the SQL syntax supported by Advantage. In general, command text in the Command object supports row-returning queries, action queries, and stored procedures.

The following tables list the features available with a Command object opened with this provider.

Availability of standard ADO 2.1 Command methods:

| Method | Supported? | Comments |
| Cancel | Yes | Canceling a synchronous command is supported if it is canceled from another thread. Canceling an asynchronous command is not supported because asynchronous commands are not supported. |
| CreateParameter | Yes |  |
| Execute | Yes | Executing asynchronous commands is not supported. The parameters RecordsAffected and Parameters are both fully supported. |

Availability of standard ADO 2.1 Command properties:

| Property | Availability | Comments |
| ActiveConnection | read/write |  |
| CommandText | read/write | Must be an SQL statement. Asynchronous commands are not supported. |
| CommandTimeout | read/write | Indicates how long to wait while executing an SQL query before terminating the attempt and generating an error. Default is 30 seconds. Specifying a value of 0 means there is no timeout. |
| CommandType | read/write | Supported values are adCmdText, adCmdTable, adCmdTableDirect, and adCmdStoredProc. If it is adCmdText, the command is expected to be a valid SQL statement. If it is adCmdTable or adCmdTableDirect, the command is expected to be a table name. The difference between these two is that adCmdTable causes ADO to generate a SELECT statement using the given table name and the OLE DB Command object is used to execute the query. With adCmdTableDirect, ADO opens the table directly through an OLE DB Rowset object. If the CommandType is adCmdStoredProc, the command is expected to be a stored procedure (Advantage Extended Procedure) name. If the stored procedure has parameters, they must be provided with the command text enclosed in parentheses. |
| Name | read/write |  |
| Prepared | read/write |  |
| State | always adStateClosed  or adStateOpen | Asynchronous operations are not supported. |

Advantage allows the cursor type be specified as adOpenForwardOnly or adOpenDynamic. If adOpenDynamic is specified, the provider will return either a dynamic cursor or a static cursor and reset the CursorType property to indicate the type of Recordset returned based on the SQL statement. For example, SQL joins result in static cursors even if adOpenDynamic is specified. Forward-only cursors may be useful when reading through a cursor in a single pass for batch processing operations. Note that forward-only cursors may be edited, but this negates the benefits. Your application should use a dynamic cursor if you plan to edit it. See [Read-Ahead Record Caching](master_read_ahead_record_caching.md) for more information.
