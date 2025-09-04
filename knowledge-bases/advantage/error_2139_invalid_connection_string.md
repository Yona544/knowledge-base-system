2139 Invalid connection string




Advantage Database Server 12  

2139 Invalid connection string

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2139 Invalid connection string  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2139 Invalid connection string Advantage Error Guide error\_2139\_invalid\_connection\_string Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2139 Invalid connection string  Advantage Error Guide |  |  |  |  |

Problem: An invalid connection string is specified.

Solution: This error indicates an internal problem in the Advantage SQL Engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.