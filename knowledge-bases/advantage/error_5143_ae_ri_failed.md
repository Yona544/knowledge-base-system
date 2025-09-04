5143 AE\_RI\_FAILED




Advantage Database Server 12  

5143 AE\_RI\_FAILED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5143 AE\_RI\_FAILED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5143 AE\_RI\_FAILED Advantage Error Guide error\_5143\_ae\_ri\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5143 AE\_RI\_FAILED  Advantage Error Guide |  |  |  |  |

Problem: The new referential integrity rule could not be added to the Advantage Data Dictionary.

Solution: When this error occurs, retrieve the text error message that accompanies the error code. That text will include the specific reason that the new rule failed to be added. Some causes are:

|  |  |
| --- | --- |
| · | The primary key name supplied is not the primary index for the table. |

|  |  |
| --- | --- |
| · | The primary key and foreign key are not the same length. |

|  |  |
| --- | --- |
| · | The primary key and foreign key do not consist of the same number of fields. |

|  |  |
| --- | --- |
| · | A field in the primary key has a different length than the corresponding field in the foreign key. |

|  |  |
| --- | --- |
| · | A field in the primary key has a different type than the corresponding field in the foreign key. |