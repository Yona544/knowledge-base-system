6033 Memo field does not exist




Advantage Database Server 12  

6033 Memo field does not exist

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6033 Memo field does not exist  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6033 Memo field does not exist Advantage Error Guide error\_6033\_memo\_field\_does\_not\_exist Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6033 Memo field does not exist  Advantage Error Guide |  |  |  |  |

Problem: A memo field name specified in an operation does not exist. Currently, functions that specify a memo field name are AX\_BLOB2File() and AX\_File2BLOB().

Solution: Make sure the specified memo field exists in the table that is being used before attempting an operation requiring that memo field.