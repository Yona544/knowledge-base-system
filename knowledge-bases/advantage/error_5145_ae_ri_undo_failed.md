5145 AE\_RI\_UNDO\_FAILED




Advantage Database Server 12  

5145 AE\_RI\_UNDO\_FAILED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5145 AE\_RI\_UNDO\_FAILED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5145 AE\_RI\_UNDO\_FAILED Advantage Error Guide error\_5145\_ae\_ri\_undo\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5145 AE\_RI\_UNDO\_FAILED  Advantage Error Guide |  |  |  |  |

Problem: The referential integrity has been corrupted due to a write operation that failed.

Solution: The current record update was affected by an RI rule. The update caused a cascade to child records. Child records were modified. A failure occurred. All changes were attempted to be undone, but a second failure occurred. At this point, the integrity of the reference from parent to child is not guaranteed. To fix this problem, delete each RI rule and re-add it. Please report to Advantage Technical Support that this error was returned.