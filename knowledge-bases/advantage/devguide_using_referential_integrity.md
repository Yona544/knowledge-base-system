Using Referential Integrity




Advantage Database Server 12  

     Using Referential Integrity

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Referential Integrity  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Using Referential Integrity Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Referential\_Integrity Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Using Referential Integrity / Dear Support Staff, |  |
| Using Referential Integrity  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Referential integrity definitions are valuable, but they tend to get overused. Most database applications contain many related tables. But just because two tables contain related data does not mean that there is a parent/child relationship that needs to be managed through referential integrity.

There are two primary problems caused by the overuse of referential integrity definitions. The first is that few related tables require the tight controls imposed by referential integrity. Referential integrity restricts your ability to delete and change parent table records, as well as prohibiting the insertion of child records for which there is no parent. When applied to the wrong tables, a user's attempt to add, edit, or delete data may be rejected, even when that operation is legitimate.

The second problem is related to resources. Whenever a table involved in a referential integrity definition is written to, the associated tables and their auto-open indexes are opened. This happens even if you are making a change only to the one table you opened.

Extensive use of referential integrity may require you to configure Advantage to use additional work areas to handle the increases in table usage, and can also make it more difficult to obtain an exclusive lock on a table. (A table opened as a result of a referential integrity definition cannot be opened exclusively by another user.)

The solution is to use referential integrity sparingly. Most applications have only one or two pairs of tables whose related data is so critical to the application that referential integrity definitions are required. For many other related but nonessential tables, the data integrity provided by referential integrity is not worth the restrictions and increased resource usage they produce.

 

In the next chapter you will learn how to create and use views.