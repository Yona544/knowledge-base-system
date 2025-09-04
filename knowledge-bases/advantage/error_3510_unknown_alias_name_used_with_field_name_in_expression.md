3510 Unknown alias name used with field name in expression




Advantage Database Server 12  

3510 Unknown alias name used with field name in expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3510 Unknown alias name used with field name in expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3510 Unknown alias name used with field name in expression Advantage Error Guide error\_3510\_unknown\_alias\_name\_used\_with\_field\_name\_in\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3510 Unknown alias name used with field name in expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.