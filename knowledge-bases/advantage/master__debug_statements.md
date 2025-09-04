::DEBUG\_STATEMENTS




Advantage Database Server 12  

::DEBUG\_STATEMENTS

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ::DEBUG\_STATEMENTS |  |  | Feedback on: Advantage Database Server 12 - ::DEBUG\_STATEMENTS master\_\_debug\_statements Advantage SQL > Debugging SQL Script > SQL Debugging Tables > ::DEBUG\_STATEMENTS / Dear Support Staff, |  |
| ::DEBUG\_STATEMENTS |  |  |  |  |

The ::DEBUG\_STATEMENTS table holds information about the query handles currently being debugged.

Definition

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| user\_id | Integer | 4 | Foreign key into the ::DEBUG\_CONNECTIONS table. |
| query\_id | Integer | 4 | Primary key of the table. |
| stmt\_name | Char | 32 | Name of the query handle. The value of this column may be used in DEBUG commands where a statement\_name value is required.  This value can also be obtained from ::stmt.name system variable. |