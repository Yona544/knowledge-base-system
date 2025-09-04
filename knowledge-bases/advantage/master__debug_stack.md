::DEBUG\_STACK




Advantage Database Server 12  

::DEBUG\_STACK

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ::DEBUG\_STACK |  |  | Feedback on: Advantage Database Server 12 - ::DEBUG\_STACK master\_\_debug\_stack Advantage SQL > Debugging SQL Script > SQL Debugging Tables > ::DEBUG\_STACK / Dear Support Staff, |  |
| ::DEBUG\_STACK |  |  |  |  |

The ::DEBUG\_STACK table holds information about suspended debuggees.

Definition

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| user\_id | Integer | 4 | Foreign key to the [::DEBUG\_CONNECTIONS](master__debug_connections.htm) table. |
| stack\_frame | autoinc | 4 | Part of the primary key of the table. |
| query\_id | Integer | 4 | Handle of the query where this stack frame is currently executing. The value in the column may not correspond to any value in the [::DEBUG\_STATEMENTS](master__debug_statements.htm) table. It is used internally. |
| source\_id | Integer | 4 | Foreign key to the [::DEBUG\_SOURCES](master__debug_sources.htm) table. |
| source\_offset | Integer | 4 | The location in the source code for this stack frames execution point. |
| stmt\_end | Integer | 4 | The location in the source where the currently executing statement ends. |
| Line | Integer | 4 | The line number in the current SQL script where execution was suspended. |
| souce\_object | Varchar | 68 | The name of the object the current stack frame is referencing. It is in the form [ParentID].ObjectName if the current frame references a database object. It may also be NULL or "Base Script". The same information is available in the [::DEBUG\_SOURCES](master__debug_sources.htm) table. |
| stmt\_name | Char | 32 | Name of the query handle. |

Remarks

The ::DEBUG\_STACK table is the most important table for presenting information for human consumption. The primary key for the table has the expression "user\_id;descend(stack\_frame)". By setting a scope using the user\_id as the partial key, the execution stack can be traversed from the top, where the execution has been suspended, to the bottom, where the query engine was first entered.

The information in the table is only valid for the suspended debuggees.