5225 Delta Support Not Possible




Advantage Database Server 12  

5225 Delta Support Not Possible

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5225 Delta Support Not Possible  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5225 Delta Support Not Possible Advantage Error Guide Error\_5225\_delta\_support\_not\_p Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5225 Delta Support Not Possible  Advantage Error Guide |  |  |  |  |

Problem: Cannot enable oData server Delta functionality for the table because requirements are not met.

Solution: To support the Delta functional, the table must meet the following requirements:

|  |  |
| --- | --- |
| 1. | The table must have a ROWVERSION column. |

|  |  |
| --- | --- |
| 2. | The table must have a Unique Index, Primary Key or Autoinc field. |

Additionally, the data dictionary must be allowed to create a table named "GetTombstones". If there is an object with this name already exists in the data dictionary, and it does not have the right fields to support the delta functionality, then this error may be returned. If that is the case, removing the "GetTombstones" object and re-enabling the Delta support for the table should solve the problem.