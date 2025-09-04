5179 AE\_VALUE\_OVERFLOW




Advantage Database Server 12  

5179 AE\_VALUE\_OVERFLOW

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5179 AE\_VALUE\_OVERFLOW  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5179 AE\_VALUE\_OVERFLOW Advantage Error Guide error\_5179\_ae\_value\_overflow Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5179 AE\_VALUE\_OVERFLOW  Advantage Error Guide |  |  |  |  |

Problem: The value cannot be stored in the designated column. For example: this error will be returned when attempting to store into an Integer column a numeric value that is outside the range -2,147,483,647 to 2,147,483,647. See [ADT Field Types and Specification](master_adt_field_types_and_specifications.htm).

Solution: Ensure the numeric value to be stored in a column is within the supported range or restructure (i.e., ALTER) the table to ensure that the column can stored the expected values.