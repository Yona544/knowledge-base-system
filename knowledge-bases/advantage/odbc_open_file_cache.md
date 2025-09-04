Open File Cache




Advantage Database Server 12  

Open File Cache

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Open File Cache |  |  | Feedback on: Advantage Database Server 12 - Open File Cache odbc\_Open\_file\_cache Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Open File Cache |  |  |  |  |

This numeric value determines the maximum number of unused file opens to cache. When tables are opened, the Advantage ODBC Driver keeps them open. This provides better performance by preventing the Driver from performing another open if another query uses one of the tables. The advantage of open file caching is increased performance. The disadvantage is that a user may receive a locking conflict even though no one appears to have the file open.

As a default, Open File Cache is set to 5. You can further increase performance by setting Open File Cache to a higher number, such as "10".