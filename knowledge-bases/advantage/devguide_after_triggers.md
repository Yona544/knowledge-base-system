AFTER Triggers




Advantage Database Server 12  

     AFTER Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AFTER Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      AFTER Triggers Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_AFTER\_Triggers Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > AFTER Triggers / Dear Support Staff, |  |
| AFTER Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

AFTER triggers execute following the successful insertion, deletion, or modification of a record. For example, you can use AFTER triggers to perform notifications. Imagine that you have a special table in your database where errors are logged. Imagine further that these error records have a field indicating the severity of the error. After an error is inserted into the error database, the trigger can inspect the severity of the error, and if severe enough, send an email to the network administrator or the help desk.

As of Advantage 8, AFTER triggers can also make changes to a record being inserted or updated. For example, from an AFTER INSERT or UPDATE trigger, your trigger code could write the user name associated with the connection, as well as the application ID of the client application, to the record inserted or updated. AFTER triggers like these are easier to write than INSTEAD OF triggers that would otherwise perform the same task. This is because from the AFTER trigger, the inserted or updated data has already been written to the underlying record. From an INSTEAD OF trigger, your code would have to write all data, not just the user name and application ID.

If you want to implement notification, but your table already includes an INSTEAD OF trigger, perform the notification inside of the INSTEAD OF trigger, because an AFTER trigger will not be fired if an INSTEAD OF trigger exists.