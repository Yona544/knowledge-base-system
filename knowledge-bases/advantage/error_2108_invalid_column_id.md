2108 Invalid column id




Advantage Database Server 12  

2108 Invalid column id

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2108 Invalid column id  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2108 Invalid column id Advantage Error Guide error\_2108\_invalid\_column\_id Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2108 Invalid column id  Advantage Error Guide |  |  |  |  |

Problem: An invalid column id is used.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.