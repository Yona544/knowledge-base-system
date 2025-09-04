Trigger Priority




Advantage Database Server 12  

     Trigger Priority

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Trigger Priority  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Trigger Priority Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Trigger\_Priority Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Trigger Priority / Dear Support Staff, |  |
| Trigger Priority  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When you define a trigger, you can assign a value to it that identifies the priority of the trigger. Trigger priority is used when you have two or more triggers of the same trigger type and event type on a given table. The trigger with a lower priority value gets executed before triggers with a higher priority value.

For example, imagine that you have two AFTER insert triggers on a particular table. If one of these triggers has a priority of 1, and the other has a priority of 2, the trigger with a priority of 1 will execute first, followed by the trigger with a priority of 2.

Trigger priority only applies to BEFORE and AFTER triggers. It does not apply to INSTEAD OF triggers. This is because you can have only one INSTEAD OF trigger for a given event type per table.