7036 Failed transaction recovery error




Advantage Database Server 12  

7036 Failed transaction recovery error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7036 Failed transaction recovery error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7036 Failed transaction recovery error Advantage Error Guide error\_7036\_failed\_transaction\_recovery\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7036 Failed transaction recovery error  Advantage Error Guide |  |  |  |  |

Problem: A failed transaction recovery was not successful.

Solution: Make sure the table or index files associated with the failed transaction were not opened by another application. This error can also occur if the transaction log file could not be opened. Refer to the error log file (ADS\_ERR.ADT or ADS\_ERR.DBF) for more specific errors related to this failure.