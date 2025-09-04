2125 Invalid table name




Advantage Database Server 12  

2125 Invalid table name

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2125 Invalid table name  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2125 Invalid table name Advantage Error Guide error\_2125\_invalid\_table\_name Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2125 Invalid table name  Advantage Error Guide |  |  |  |  |

Problem 1: The SQL statement contains a table name that is too long.

Solution 1: Verify that the combined connect path and table name is 255 characters or less.

Problem 2: A drive letter is used in the table name and the Advantage Database Server is used to execute the SQL statement. For example, "SELECT \* INTO "c:\temp\tmpTable" FROM MyTable" or "CREATE TABLE "c:\temp\tmpTable" ( fld1 integer )". Because the drive letter mappings of the Advantage Database Server is likely to be different from the client computer's drive letter mappings, a drive letter is not allowed when executing SQL statements that require creating a table.

Solution 2: Use a UNC path or relative path. For example, "SELECT \* INTO "\\MyAdsServer\temp\tmpTable" FROM MyTable".