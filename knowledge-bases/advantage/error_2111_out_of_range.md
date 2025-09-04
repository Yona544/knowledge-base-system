2111 Out of range




Advantage Database Server 12  

2111 Out of range

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2111 Out of range  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2111 Out of range Advantage Error Guide error\_2111\_out\_of\_range Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2111 Out of range  Advantage Error Guide |  |  |  |  |

Problem: A data conversion within the SQL engine exceeded the range of the target value. For example, a parameter value stored as a double may have exceeded a short integer field range. Or there is data corruption in the tables used by the SQL query.

Solutions:

|  |  |
| --- | --- |
| 1. | Verify that the statement is using compatible data types. |

|  |  |
| --- | --- |
| 2. | Verify that there is no corruption in the tables used by the SQL query, especially that there is no corruption in the date, time, or timestamp columns in the tables. |