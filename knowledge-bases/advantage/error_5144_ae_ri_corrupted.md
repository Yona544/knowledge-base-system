5144 AE\_RI\_CORRUPTED




Advantage Database Server 12  

5144 AE\_RI\_CORRUPTED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5144 AE\_RI\_CORRUPTED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5144 AE\_RI\_CORRUPTED Advantage Error Guide error\_5144\_ae\_ri\_corrupted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5144 AE\_RI\_CORRUPTED  Advantage Error Guide |  |  |  |  |

Problem: The referential integrity has been corrupted due to a delete operation that failed.

Solution: The current record update was affected by an RI rule. The update caused a cascade to child records. Records were deleted. A failure occurred. All changes were attempted to be undone, but a record could not be deleted. At this point, the integrity of the reference from parent to child is not guaranteed. To fix this problem, delete each RI rule and re-add it. Please report to Advantage Technical Support that this error was returned.