2131 Value in an IN expression must be a simple value




Advantage Database Server 12  

2131 Value in an IN expression must be a simple value

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2131 Value in an IN expression must be a simple value  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2131 Value in an IN expression must be a simple value Advantage Error Guide error\_2131\_value\_in\_an\_in\_expression\_must\_be\_a\_simple\_value Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2131 Value in an IN expression must be a simple value  Advantage Error Guide |  |  |  |  |

Problem: The IN clause in the SQL statement contains an invalid value. For example, "SELECT \* FROM mytable WHERE field IN (2\*3)" is not valid.

Solution: The values in the IN clause must be simple constants, parameters, or the USER literal.