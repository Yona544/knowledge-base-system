Views As Temporary Tables




Advantage Database Server 12  

     Views As Temporary Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Views As Temporary Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Views As Temporary Tables Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Views\_As\_Temporary\_Tables Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Views As Temporary Tables / Dear Support Staff, |  |
| Views As Temporary Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Some operations cannot be performed using a single query. For example, you may need to execute one query to create a result set with intermediate results. You then use the first query's result in another query. Situations like these often call for the creation of a temporary table that will be used to store the intermediate results, so that the second query can be executed against these records.

Views provide an alternative to temporary tables. Consider the Sum by Invoice view created in the preceding section. This view returns the type of data that you could have placed into a temporary table. Then, a query similar to the one you entered into the Sales by Employee view could have been used to process the records in this temporary table. The use of views made the creation of a temporary table unnecessary.

Whether you use views or temporary tables depends on the needs of your application. With views, the result returned by a view is available only until you close the view. A temporary table, by comparison, is available until the connection is closed. Temporary tables are unique to each connection, and, unless specifically dropped from within the connection, are not destroyed until the connection is closed. Temporary tables are discussed further in Chapter 11.

There is another important difference between views and temporary tables. When you are using ADS, the result set returned by an editable view is dynamic. Specifically, the records that constitute the result set of a view can change as other users post data to the database. By comparison, the contents of a temporary table are static, in that they only hold those records specifically added to the temporary table.