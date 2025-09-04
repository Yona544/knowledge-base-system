2223 Cursor is not on a valid row




Advantage Database Server 12  

2223 Cursor is not on a valid row

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2223 Cursor is not on a valid row  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2223 Cursor is not on a valid row Advantage Error Guide error\_2223\_cursor\_is\_not\_on\_a\_valid\_row Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2223 Cursor is not on a valid row  Advantage Error Guide |  |  |  |  |

Problem: Data from the column could not be read because the cursor is not on a valid row. The row pointer is either before the first row or after the last row in the cursor.

Solution: Check the error message for the location of the error in the script. Verify that FETCH is called on the cursor before reading the column data and that the result from the FETCH statement is checked before trying to access the data.