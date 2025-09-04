2229 Ambiguous reference in the SQL script




Advantage Database Server 12  

2229 Ambiguous reference in the SQL script

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2229 Ambiguous reference in the SQL script  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2229 Ambiguous reference in the SQL script Advantage Error Guide error\_2229\_ambiguous\_reference\_in\_the\_sql\_script Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2229 Ambiguous reference in the SQL script  Advantage Error Guide |  |  |  |  |

Problem: An identifier used in an SQL statement is ambiguous. It may reference either a table column or a script variable.

Solution: Check the error message for the location of the error in the script and determine the intended purpose for the identifier. Depending on the intended purpose of the identifier, the conflict may be resolved by either changing the name of the variable (see [DECLARE](master_declare.htm) or making a explicit column reference using the TableAlias.ColumnName notation.