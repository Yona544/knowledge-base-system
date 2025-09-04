Exclusive Locks and Cursor Caching




Advantage Database Server 12  

     Exclusive Locks and Cursor Caching

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Exclusive Locks and Cursor Caching  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Exclusive Locks and Cursor Caching Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Exclusive\_Locks\_and\_Cursor\_Caching Advantage Developer's Guide > Appendixes > Appendix B - Troubleshooting and Other Issues > Exclusive Locks and Cursor Caching / Dear Support Staff, |  |
| Exclusive Locks and Cursor Caching  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADS is a high-performance server; it uses a number of advanced techniques for optimizing the operations that it performs. One of these optimizations is to keep the cursor of a SELECT query in cache following the execution of the query. This technique improves performance since there is a high likelihood that a just executed query will be executed again very soon.

While this optimization increases performance, it has one potential drawback. If you are working in an environment that permits you to place an exclusive lock on a table, that lock will fail if the table you are locking has an open cursor in the cursor cache. In other words, an exclusive lock may fail even though the table being locked is not actually being used by another user.

For those development environments that permit exclusive table locks, such as Delphi or .NET, or any development language that can make direct calls to the ACE (Advantage Client Engine) API (such as Delphi, Visual Basic, Visual C++, and C++Builder), there is a way to disable cursor caching. In short, you either call the AdsCloseCachedTables function to close all cursors in the cache or set the size of the cursor cache to 0.

A similar effect can occur with respect to SQL statements. If an exclusive lock cannot be obtained on a table involved in a query, use AdsCloseSQLStatement to release the resources associated with the query.