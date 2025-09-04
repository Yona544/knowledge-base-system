How Many Indexes Should You Define?




Advantage Database Server 12  

     How Many Indexes Should You Define?

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How Many Indexes Should You Define?  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      How Many Indexes Should You Define? Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_How\_Many\_Indexes\_Should\_You\_Define\_ Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > How Many Indexes Should You Define? / Dear Support Staff, |  |
| How Many Indexes Should You Define?  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As is the case with so many issues in software development, there are trade-offs between the number of indexes and performance. The more indexes you have on a table, the more work Advantage has to perform in the background as you modify the contents of your table. For every record that is inserted, deleted, or modified, the tables associated indexes must be updated.

In the end, it is a balancing act. You dont want to have too few or too many indexes. In general, you want to ensure that you have indexes to support those operations that are performed frequently, and that must be performed quickly. For those operations that are performed only occasionally, or for which performance is not an issue, additional indexes should be defined only if they do not reduce performance in other areas.

For instance, if your table has only a few indexes, and their updates at runtime is not noticeable, it wont hurt to add an additional index for non-critical tasks. On the other hand, if your table already has many indexes, and their runtime update is a performance concern, you may not want to add additional, nonessential indexes.