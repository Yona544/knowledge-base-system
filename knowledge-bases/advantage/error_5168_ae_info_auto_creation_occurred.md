5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED




Advantage Database Server 12  

5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED Advantage Error Guide error\_5168\_ae\_info\_auto\_creation\_occurred Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5168 AE\_INFO\_AUTO\_CREATION\_OCCURRED  Advantage Error Guide |  |  |  |  |

This error code is never returned to the client. It will only appear in error logs should a dictionary tables auto-creation property be set to True and the tables file and/or index files not exist and require re-creation.

Note This code serves as verification that auto-creation successfully took place. It is a sign that auto-creation is working properly and to list any files that were re-created.

 

Note This code is preceded by several "File Not Found" error codes in the error log (7041 errors). This is normal behavior.