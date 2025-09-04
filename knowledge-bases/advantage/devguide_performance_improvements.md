Performance Improvements




Advantage Database Server 12  

     Performance Improvements

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Performance Improvements  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Performance Improvements Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Performance\_Improvements Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Performance Improvements / Dear Support Staff, |  |
| Performance Improvements  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage is known for its exceptional performance, due to the emphasis that the Advantage team places on speed. So it's not surprising that they have continued to tweak Advantage to make it even faster.

Advantage 8 adds additional caching and optimizations, resulting in better performance than ever. Areas that benefit from this work include index access, transaction processing, SQL statements that use subqueries or views in the FROM clause, client/server communication on a single machine, and static queries with multiple simultaneous users.

In addition, Advantage 8 was compiled to take advantage of the improved memory address capabilities of 64-bit processors. As a result, Advantage can address up to four gigabytes of memory on a 64-bit processor. Even on 32-bit processors, Advantage 8 can address as much as three gigabytes of memory (when the /3G switch appears in the boot.ini file), a 50 percent improvement over previous versions.