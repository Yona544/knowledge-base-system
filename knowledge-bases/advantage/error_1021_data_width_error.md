1021 Data Width Error




Advantage Database Server 12  

1021 Data Width Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1021 Data Width Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 1021 Data Width Error Advantage Error Guide error\_1021\_data\_width\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 1021 Data Width Error  Advantage Error Guide |  |  |  |  |

Problem: The value assigned to a numeric FIELD variable could not be accurately represented in the field width specified by the database structure.

Solution: Change the program to suppress invalid values or modify the structure of the table to allow for larger values.

Note The default handling for this error is to fill the relevant part of the physical table record with asterisk (\*) characters. Subsequent accesses to the field will produce a value of zero until a new value is assigned.