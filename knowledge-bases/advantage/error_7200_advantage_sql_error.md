7200 Advantage SQL Error




Advantage Database Server 12  

7200 Advantage SQL Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7200 Advantage SQL Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7200 Advantage SQL Error Advantage Error Guide error\_7200\_advantage\_sql\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7200 Advantage SQL Error  Advantage Error Guide |  |  |  |  |

Problem: The problem might be caused by an SQL statement error or some other limitation in the way Advantage processes SQL statements.

Solution: Use AdsGetLastError to retrieve a detailed description of the error. The error description contains a "NativeError" code that you can look up. An example error string might be as follows:

Error 7200: AQE Error: State = HY000; NativeError = 5012; [Extended Systems][Advantage SQL][ASA] Error 5012.

In this case, you would look up error [5012](error_5012_ae_invalid_fielddef.htm) to get more detailed information. The native error codes can, in general, be Advantage Client Engine errors (5000+), Advantage Database Server errors (7000+), or an SQL-specific error. Note that the SQL-specific error code values may change in a future release.

If you get a native error code that is not documented, contact [Technical Support](master_technical_support_u_s__and_canada.htm).