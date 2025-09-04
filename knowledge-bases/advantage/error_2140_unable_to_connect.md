2140 Unable to connect




Advantage Database Server 12  

2140 Unable to connect

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2140 Unable to connect  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2140 Unable to connect Advantage Error Guide error\_2140\_unable\_to\_connect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2140 Unable to connect  Advantage Error Guide |  |  |  |  |

Problem: Unable to connect to Advantage Database Server or Advantage Local Server

Solution: This error indicates an internal problem in the Advantage SQL engine. In general, this error should not be returned to the application directly. If the application does receive this error, the SQL statement handle should not be used any further. Close the existing SQL statement handle and create and use a new one. Please report the error with a small sample application demonstrating the issue to Advantage Technical Support at advantage@extendsys.com.