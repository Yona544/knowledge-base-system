---
title: Master System Variables
slug: master_system_variables
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_variables.htm
source: Advantage CHM
tags:
  - master
checksum: 72bbaf4321fff672e2a41146267a82ef57467238
---

# Master System Variables

System Variables

System Variables

Advantage SQL Engine

| System Variables  Advantage SQL Engine |  |  |  |  |

The Advantage Query Engine maintains two categories of system variables. The first category of system variable returns information about the current user connection or information about the current query handle. These variables are prefixed with the :: (double colons) followed by "server", "conn." or "stmt.", short hand for server, connection or statement (query handle) respectively. The second category of system variables are maintained by the SQL Script Execution Engine for the purpose of error handling. These variables are denoted by the double underscore-characters, "\_\_", leading the variable name.

Server Level Variables

| Variable Name | Description |
| ::server.OldestActiveTxn | Timestamp. Returns the starting time of the oldest active transaction on the server. NULL is returned if there is no transaction active on the server. |

Connection Level Variables

| Variable Name | Description |
| ::conn.Name | Character string. Returns the name of the current user connection. The connection name is unique for each connection and it is used by the SQL debugger. |
| ::conn.Collation | Character String. Default collation for statements allocated on the current connection. This variable is settable. See [SET <system variable>](master_set_system_variable_.md). |
| ::conn.TransactionCount | Integer. Returns the [nesting](master_nesting_transactions.md) depth of the current transaction or 0 if one has not been started. |
| ::conn.OperationCount | Integer. Returns the number of operations performed by the server for this connection. |
| ::conn.OSUserLoginName | Character string.  Returns the OS user login name. |
| ::conn.ClientHostName | Character string.  Returns the computer name of the user. |
| ::conn.NetworkAddress | Character string.  Returns the IP address of the connected user for networked connections. With local server connections, this will be empty. For shared memory connections, this contains a string showing the IPC connection number. |
| ::conn.TerminalClientAddress | Character string.  Returns the IP address of the Terminal Services client if the connection is made from a Terminal Server. |
| ::conn.IsRoot | Logical value that indicates if the current connection is to the [root dictionary](master_root_dictionary.md). |

Statement Level Variables

| Variable Name | Description |
| ::stmt.Name | Character string. Returns the name of the current query handle. The statement name is unique for each query handle and it stays unchanged as long as the query handle is valid regardless the number of individual statements executed on the query handle. This variable is used by the SQL debugger. |
| ::stmt.UpdateCount | Returns the number of rows affected since the beginning of the current execution. |
| ::stmt.TrigRecNo | Integer. Returns the record number of the row that led to the firing of the trigger. This variable is only meaningful when accessed inside a trigger script. |
| ::stmt.TrigRowid | Char(18). Returns the [ROWID](master_rowid.md) of the row that led to the firing of the trigger. This variable is only meaningful when accessed inside a trigger script. ROWID is similar to record number but it is more useful in SQL statements and scripts. |
| ::stmt.TrigName | Character String. Returns the name of the trigger object being fired. This variable is only meaningful when accessed inside of a trigger script. |
| ::stmt.TrigTableName | Character String. Returns the name of the table object that is being updated and caused the trigger to fire. This variable is only meaningful when accessed inside of a trigger script. |
| ::stmt.TrigEventType | Integer. Returns the type of event that led to the firing of the trigger. This variable is only meaningful when accessed inside of a trigger script. See [CREATE TRIGGER](master_create_trigger.md). |
| ::stmt.TrigType | Integer. Returns the type of trigger being fired. This variable is only meaningful when accessed inside of a trigger script. See [CREATE TRIGGER](master_create_trigger.md). |
| ::stmt.Collation | Character String. Collation language for sorting and comparing character data when executing SQL statements on this statement handle. This variable is settable. See [SET <system variable>](master_set_system_variable_.md). |
| ::stmt.unicode\_sort\_key\_size | Integer. This variable is settable. See [SET <system variable>](master_set_system_variable_.md). The value of this variable controls the key size multiplier of the Unicode data when sorting is required, such as GROUP BY or ORDER BY. The accepted range is 1 - 8 and the default is 3. When sorting Unicode data, the key for each Unicode character can 1 or more bytes. Common Latin character needs 1 to 2 bytes for the sort key. Characters in Eastern language may take up to 5 bytes for each character. Unusual characters, such as ß, may take more than 5 bytes per character. When sorting of Unicode string is required, SQL engine pre-allocates a sort key buffer that is roughly (maximum\_string\_length X unicode\_sort\_key\_size). If the actual key is longer than the pre-allocated key buffer size, the key is truncated and the result of the sort may be unpredictable. Setting the ::stmt.unicode\_sort\_key\_size to a larger value will guarantee the result of the sort but will cause decreased performance. |

Script Error Handling Variables

The variables in this category are \_\_errclass (String), \_\_errcode (Integer), and \_\_errtext (String). These three variables provide information about an exception in the script, either a raised exception or a runtime error. They are local to the current executing SQL script. They cannot be assigned values directly using assignment statements. Instead, their values are initialized when a RAISE statement is executed or when a runtime error is detected. If the exception originates from a [RAISE](master_raise.md) statement, these three variables will be assigned the values provided by the RAISE statement. If the exception is caused by a runtime error, the \_\_errclass variable will be initialized with string value "ADS\_SCRIPT\_EXCEPTION" and the \_\_errcode and \_\_errtext variables will contain the error code and error text that will be returned to the caller if the exception is not handled.
