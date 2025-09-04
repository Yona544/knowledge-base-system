::DEBUG\_BREAKS




Advantage Database Server 12  

::DEBUG\_BREAKS

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ::DEBUG\_BREAKS |  |  | Feedback on: Advantage Database Server 12 - ::DEBUG\_BREAKS master\_\_debug\_breaks Advantage SQL > Debugging SQL Script > SQL Debugging Tables > ::DEBUG\_BREAKS / Dear Support Staff, |  |
| ::DEBUG\_BREAKS |  |  |  |  |

The ::DEBUG\_BREAKS table holds information about all break points defined for the current debugger session.

Definition

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| break\_name | CiChar | 43 | Name of the break point. The value in this column may be null. |
| user\_id | Integer | 4 | Non-zero if the break point should only apply to the specific user. The value in this column may be null. |
| query\_id | Integer | 4 | Non-zero if the break point should only apply to the specific query handle. The value in this column may be null. |
| object\_id | Integer | 4 | Non-zero if the break point is set for an object in the database. Otherwise the break point if for the base script. |
| Offset | Integer | 4 | Location in the source script where the break point is set. |
| ObjectType | Short | 2 | Non-zero if the object\_id is non-zero. Identifies the type of the object in the database. Possible values are ADS\_DD\_FUNCTION\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT or ADS\_DD\_TRIGGER\_OBJECT. These constants are defined in the header file ace.h. |

Remark

When an SQL script is executed in debug mode, the ::DEBUG\_BREAKS table is consulted by the query engine to determine whether execution should be suspended. If a break point matching the current executing script is found, the execution is suspended and the [::DEBUG\_CONNECTIONS](master__debug_connections.htm) table is updated.

See [DEBUG BREAK POINT](master_debug_break_point.htm) statement for additional information.