3010 Unknown alias name used with field name in index key expression




Advantage Database Server 12  

3010 Unknown alias name used with field name in index key expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3010 Unknown alias name used with field name in index key expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3010 Unknown alias name used with field name in index key expression Advantage Error Guide error\_3010\_unknown\_alias\_name\_used\_with\_field\_name\_in\_index\_key\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3010 Unknown alias name used with field name in index key expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the key expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.