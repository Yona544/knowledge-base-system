2142 - 2144 Internal Error




Advantage Database Server 12  

2142 - 2144 Internal Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2142 - 2144 Internal Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2142 - 2144 Internal Error Advantage Error Guide error\_2142\_2144\_internal\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2142 - 2144 Internal Error  Advantage Error Guide |  |  |  |  |

Problem: Internal error.

Solution: This error indicates an internal problem in the Advantage SQL Engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.