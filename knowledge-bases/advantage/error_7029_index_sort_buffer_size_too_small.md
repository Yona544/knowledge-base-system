7029 Index Sort Buffer Size too small




Advantage Database Server 12  

7029 Index Sort Buffer Size too small

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7029 Index Sort Buffer Size too small  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7029 Index Sort Buffer Size too small Advantage Error Guide error\_7029\_index\_sort\_buffer\_size\_too\_small Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7029 Index Sort Buffer Size too small  Advantage Error Guide |  |  |  |  |

Problem: The Index Sort Buffer Size is not large enough for an index to be built on the server.

Solution: Restart/reload the Advantage server with a larger Index Sort Buffer Size. The Index Sort Buffer Size configuration key word is SORT\_BUFFER. The default sort buffer size is 8192 Kbytes. The range for this setting is 1 to 65535 Kbytes. The equation for calculating the minimum Index Sort Buffer Size is located in an Index Sort Buffer Size entry in the Advantage knowledge base. Search for SORT\_BUFFER.