8030 Math function error




Advantage Database Server 12  

8030 Math function error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 8030 Math function error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 8030 Math function error Advantage Error Guide error\_8030\_math\_function\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 8030 Math function error  Advantage Error Guide |  |  |  |  |

Problem: An error (such as a domain error) occurred in a math library function. For example, a negative value was passed to the function that computes square roots.

Solution: The most likely cause of this error is the invalid use of a math function in an SQL statement. For example, the statement "SELECT sqrt( field ) FROM test" would generate the error if the field value was negative in any records. Verify that valid domain values are used in all math functions.

Errors in the 8000 range are returned when the Advantage server makes a direct call to an OS API, and that function returns a failure. If you receive an error in the 8000 range, retry the database operation. If the error condition persists, please send a small re-creation to Advantage [Technical Support](master_technical_support_u_s__and_canada.htm) demonstrating the problem so that Advantage R&D can investigate the issue.