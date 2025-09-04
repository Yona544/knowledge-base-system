2104 Invalid cursor name




Advantage Database Server 12  

2104 Invalid cursor name

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2104 Invalid cursor name  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2104 Invalid cursor name Advantage Error Guide error\_2104\_invalid\_cursor\_name Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2104 Invalid cursor name  Advantage Error Guide |  |  |  |  |

Problem: An invalid cursor name is specified.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.