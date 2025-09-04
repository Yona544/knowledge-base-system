::DEBUG\_VARIABLES




Advantage Database Server 12  

::DEBUG\_VARIABLES

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ::DEBUG\_VARIABLES |  |  | Feedback on: Advantage Database Server 12 - ::DEBUG\_VARIABLES master\_\_debug\_variables Advantage SQL > Debugging SQL Script > SQL Debugging Tables > ::DEBUG\_VARIABLES / Dear Support Staff, |  |
| ::DEBUG\_VARIABLES |  |  |  |  |

The ::DEBUG\_VARIABLES table contains all local variables for suspended debuggees.

Definition

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| stack\_frame | Integer | 4 | Foreign key to the "stack\_frame" column in the [::DEBUG\_STACK](master__debug_stack.htm) table. |
| var\_id | Integer | 4 | Identifies the variable. Part of the primary key. |
| var\_name | CiChar | 50 | Name of the variable or cursor column. |
| var\_type | Integer | 4 | Type of the variable. The value corresponds to the ACE field type constants defined in the header file ace.h. |
| cursor\_id | Integer | 4 | The value in this column is non-zero if the entry corresponds to a column of a cursor variable. The value in this column is zero or null if the entry is for a regular variable or cursor variable. |
| Isnull | Logical | 1 | True if the value is null. |
| char\_val | Varchar | 30 | Character representation of the value of the variable. |
| bin\_val | Binary |  | Native binary representation of the value of the variable. |
| n\_ptr | Raw | 8 | Internal ID. |
| cursor\_state | Integer | 4 | Internal ID. |

Remark

The primary key for the ::DEBUG\_VARIABLES table is "stack\_frame;cursor\_id;var\_id".