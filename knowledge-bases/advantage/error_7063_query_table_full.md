7063 Query table full




Advantage Database Server 12  

7063 Query table full

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7063 Query table full  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7063 Query table full Advantage Error Guide error\_7063\_query\_table\_full Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7063 Query table full  Advantage Error Guide |  |  |  |  |

Problem: The maximum number of configured query elements is already in use.

Solution: The maximum number of configured query elements is the same as the configured work areas. There are two possible solutions: 1) Restart/reload the Advantage server with a larger value for number of work areas; 2) Make sure that query handles are freed after they are no longer used.