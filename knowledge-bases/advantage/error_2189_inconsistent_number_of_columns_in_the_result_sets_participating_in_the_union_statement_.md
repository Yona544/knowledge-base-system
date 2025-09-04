2189 Inconsistent number of columns in the result sets participating in the UNION statement




Advantage Database Server 12  

2189 Inconsistent number of columns in the result sets participating in the UNION statement

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2189 Inconsistent number of columns in the result sets participating in the UNION statement  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2189 Inconsistent number of columns in the result sets participating in the UNION statement Advantage Error Guide error\_2189\_inconsistent\_number\_of\_columns\_in\_the\_result\_sets\_participating\_in\_the\_union\_statement\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2189 Inconsistent number of columns in the result sets participating in the UNION statement  Advantage Error Guide |  |  |  |  |

Problem: The individual queries in the UNION statement do not return the same number of columns in the result set. The queries in the UNION statement must contain the same number of columns in the result set. For example, "SELECT Lastname FROM table1 UNION SELECT lastname, firstname FROM table2" is not valid because the second SELECT returns 2 columns in the result set while the first SELECT returns only 1 column in the result set.

Solution: Adjust the SELECT clauses in the UNION statement so they all return the same number of columns.