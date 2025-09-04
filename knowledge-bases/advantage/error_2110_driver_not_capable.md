2110 Driver not capable




Advantage Database Server 12  

2110 Driver not capable

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2110 Driver not capable  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2110 Driver not capable Advantage Error Guide error\_2110\_driver\_not\_capable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2110 Driver not capable  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine cannot complete the request.

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.