ON CONFLICT Triggers




Advantage Database Server 12  

     ON CONFLICT Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ON CONFLICT Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      ON CONFLICT Triggers Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_ON\_CONFLICT\_Triggers Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > ON CONFLICT Triggers / Dear Support Staff, |  |
| ON CONFLICT Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ON CONFLICT triggers are intended for the destination tables involved in replication in order to manage replication conflicts. For example, if you have an ON CONFLICT trigger on the destination customer table, and the source table record being replicated does not match the record at the destination, your ON CONFLICT trigger can take steps to handle the conflict.

By default, conflicts are ignored and the conflicting destination table record will be replaced by the source record. However, by creating an ON CONFLICT trigger, your code can choose instead to keep the destination record, or your code can write the source record to a special table designed to holds conflicts until an administrator can evaluate the conflicting values manually.

Replication and ON CONFLICT triggers are discussed in greater detail in Chapter 10.