6010 Bad conditional index expression




Advantage Database Server 12  

6010 Bad conditional index expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6010 Bad conditional index expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6010 Bad conditional index expression Advantage Error Guide error\_6010\_bad\_conditional\_index\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6010 Bad conditional index expression  Advantage Error Guide |  |  |  |  |

Problem: An invalid expression was encountered while creating or opening an index.

Solution: Make sure the key expression (and FOR condition expression, if applicable) is a valid Xbase expression. If a User-Defined Function (UDF) is used in an expression, verify it is available in all applications that use the index.