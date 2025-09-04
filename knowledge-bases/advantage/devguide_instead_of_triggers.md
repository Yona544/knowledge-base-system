INSTEAD OF Triggers




Advantage Database Server 12  

     INSTEAD OF Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| INSTEAD OF Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      INSTEAD OF Triggers Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_INSTEAD\_OF\_Triggers Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > INSTEAD OF Triggers / Dear Support Staff, |  |
| INSTEAD OF Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

INSTEAD OF triggers replace the event they are associated with. For example, if you create an INSTEAD OF insert trigger, Advantage will not insert the associated record. If you want the record to be inserted, you must do it yourself from your trigger code.

Before an INSTEAD OF trigger fires, Advantage has already verified that the requested operation does not violate the table's field and record constraints. Note, however, that if the affected table is involved in one or more referential integrity relationships, those constraints are not applied unless the INSTEAD OF trigger completes without an error.

Using an INSTEAD OF trigger disables the execution of any AFTER triggers for the same event on the same table. If you add an INSTEAD OF trigger to a table event where there is already an AFTER trigger, move the AFTER trigger code to the INSTEAD OF trigger, and then delete the AFTER trigger definition.

INSTEAD OF triggers are a powerful tool for performing additional actions to coincide with an event. For example, you might write an INSTEAD OF trigger that tests for a null value in the first field of a table. When a null value is detected, the trigger can assign an arbitrary, unique value, such as a GUID, to the field. Unique, arbitrary keys like these ensure record uniqueness, even when records are combined from multiple sources (such as when records from individual field offices are combined together at a corporate headquarters).

Another example involves creating an audit trail. From the INSTEAD OF delete trigger you can write the values of the deleted record, as well as the time of deletion, to a special audit trail table. From the INSTEAD OF insert trigger, you can write the values of the fields being inserted, as well as the time of insertion, into the audit trail table. From the INSTEAD OF update trigger, you can write the values of the fields whose values have changed, as well as the time of the change, to the audit trail table. Importantly, so long as the trigger is being executed in a transaction, if for some reason the transaction must be rolled back, any changes written to the audit trail table in the trigger would also be rolled back. (An AFTER trigger can also be used for this purpose, but only if there is no INSTEAD OF trigger on the same event type.)

   
NOTE: If your INSTEAD OF trigger adds to, or modifies, the data while it is being written to the underlying table, it may be necessary for you to refresh that record in the client application if you want to see the new values, depending on the Advantage data access mechanism you are using.