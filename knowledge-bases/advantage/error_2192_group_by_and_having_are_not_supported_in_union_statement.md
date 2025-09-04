2192 GROUP BY and HAVING are not supported in UNION statement




Advantage Database Server 12  

2192 GROUP BY and HAVING are not supported in UNION statement

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2192 GROUP BY and HAVING are not supported in UNION statement  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2192 GROUP BY and HAVING are not supported in UNION statement Advantage Error Guide error\_2192\_group\_by\_and\_having\_are\_not\_supported\_in\_union\_statement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2192 GROUP BY and HAVING are not supported in UNION statement  Advantage Error Guide |  |  |  |  |

Problem: GROUP BY and HAVING clauses are not valid in a UNION statement. For example, "SELECT lastname, firstname FROM table1 GROUP BY lastname UNION SELECT lastname, firstname FROM table2 ORDER BY lastname" is not valid because of the GROUP BY clause in the statement. This limitation exists in the version 6.0 and earlier releases of the Advantage products.

Solution: Remove the GROUP BY or HAVING clause from the UNION statement or upgrade to the Advantage Database Server/Advantage Local Server 6.1 (or greater) release.