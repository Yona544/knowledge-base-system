2190 Incompatible column data types in the result sets participating in the UNION statement




Advantage Database Server 12  

2190 Incompatible column data types in the result sets participating in the UNION statement

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2190 Incompatible column data types in the result sets participating in the UNION statement  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2190 Incompatible column data types in the result sets participating in the UNION statement Advantage Error Guide error\_2190\_incompatible\_column\_data\_types\_in\_the\_result\_sets\_participating\_in\_the\_union\_statement\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2190 Incompatible column data types in the result sets participating in the UNION statement  Advantage Error Guide |  |  |  |  |

Problem: Each resulting column of the individual queries in the UNION statement must be the same data type for all queries. For example, "SELECT lastname FROM table1 UNION SELECT DOB FROM table2" is not valid because the second SELECT returns a column with data type of date while the first SELECT returns only a column of characters.

Solution: Adjust the SELECT clauses in the UNION statement so they all return the same data type at each column position.