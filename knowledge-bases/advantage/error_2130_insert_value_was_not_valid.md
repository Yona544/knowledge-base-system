2130 Insert value was not valid




Advantage Database Server 12  

2130 Insert value was not valid

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2130 Insert value was not valid  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2130 Insert value was not valid Advantage Error Guide error\_2130\_insert\_value\_was\_not\_valid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2130 Insert value was not valid  Advantage Error Guide |  |  |  |  |

Problem: A value in the INSERT value list was not valid. For example, "INSERT INTO mytable (field) VALUES ( sum(field2) )" is not valid.

Solution: The values in the INSERT list cannot be aggregate functions or logical expressions such as "3 < 4".