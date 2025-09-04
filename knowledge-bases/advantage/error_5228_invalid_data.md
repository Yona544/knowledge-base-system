5228 Invalid Data




Advantage Database Server 12  

5228 Invalid Data

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5228 Invalid Data  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5228 Invalid Data Advantage Error Guide Error\_5228\_invalid\_data Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5228 Invalid Data  Advantage Error Guide |  |  |  |  |

Problem: The data supplied is not valid for the given field type.

Solution:

When providing data to integer, numeric, double or long integer field as string data, make sure the string contain valid integer or numeric data. The valid data must only contain decimal digits, '.' as decimal point, and '+' or '-' sign.

When providing data to GUID field as string data, the data must be in either the registry format "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" or the same format without the '-' characters.