5152 AE\_RESTRUCTURE\_FAILED




Advantage Database Server 12  

5152 AE\_RESTRUCTURE\_FAILED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5152 AE\_RESTRUCTURE\_FAILED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5152 AE\_RESTRUCTURE\_FAILED Advantage Error Guide error\_5152\_ae\_restructure\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5152 AE\_RESTRUCTURE\_FAILED  Advantage Error Guide |  |  |  |  |

Problem: The table restructure failed.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include specifics about the error. Some causes of this problem are:

|  |  |
| --- | --- |
| · | The table was associated with user defined or custom indexes |

|  |  |
| --- | --- |
| · | A field to be deleted was in an index |

|  |  |
| --- | --- |
| · | The field to be deleted is used in the table validation expression |