Temporary Tables




Advantage Database Server 12  

     Temporary Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Temporary Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Temporary Tables Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Temporary\_Tables Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Temporary Tables / Dear Support Staff, |  |
| Temporary Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Temporary tables are like any other tables in Advantage, with several important differences. First, temporary tables are unique to a connection. Specifically, if you create a temporary table, that table is only available on the connection on which you created it (as well as to the stored procedures and triggers that execute on that connection). Because the scope of a temporary table is limited to a single connection, it is possible for two different connections to create a temporary table using the same name without name collisions.

The second major feature of temporary tables is that their lifecycle is limited to the life of the connection on which they are created. While it is possible, and in some cases desirable, to drop temporary tables during the life of a connection, it is not strictly necessary. When the connection on which a temporary table is created is closed, any temporary tables created on that connection are automatically dropped by Advantage.

A temporary table is any table whose name begins with the # character.