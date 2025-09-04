Trigger Types (BEFORE, INSTEAD OF, AFTER, and CONFLICT)




Advantage Database Server 12  

Trigger Types (BEFORE, INSTEAD OF, AFTER, and CONFLICT)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Trigger Types (BEFORE, INSTEAD OF, AFTER, and CONFLICT)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Trigger Types (BEFORE, INSTEAD OF, AFTER, and CONFLICT) Advantage Concepts master\_Trigger\_types\_before\_instead\_of\_and\_after\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Trigger Types (BEFORE, INSTEAD OF, AFTER, and CONFLICT)  Advantage Concepts |  |  |  |  |

Advantage supports four types of triggers; BEFORE, INSTEAD OF, AFTER, and CONFLICT. BEFORE triggers are fired before an insert, update, or delete operation. AFTER triggers are fired after an insert, update, or delete operation.

INSTEAD OF triggers fire before an insert, update, or delete operation. INSTEAD OF triggers replace the original operation. For example, if an INSTEAD OF DELETE trigger exists on a table, when a client deletes a record, the trigger code will fire and then control will return to the client. The server will not perform the original delete operation. INSTEAD OF triggers are useful when you want to modify the changes made by the client before actually posting the update operation.

INSTEAD OF and AFTER triggers are the only triggers allowed to modify the same record that the client application currently has locked (the operation that caused the trigger to fire in the first place). Attempts to do so with a BEFORE trigger will result in record locking errors. If your trigger code needs to modify the same record the client has locked, use an INSTEAD OF or an AFTER trigger.

INSTEAD OF triggers will often be used to slightly modify the new values being written to a table. For example, the following INSTEAD OF UPDATE trigger modifies a timestamp field each time the record is updated:

UPDATE customers SET lastupdated = now() ,

name = ( SELECT name FROM \_\_new )

WHERE id = ( SELECT id FROM \_\_new )

When a table has an INSTEAD OF trigger, it is sometimes necessary to refresh the record image after an update has been performed. This is because the trigger most likely modified the record image that the client originally updated (otherwise you could use a BEFORE trigger). For example, if using a grid and updating a record, if the trigger code modifies the record and then performs the update, the client will not know what changes the trigger made to the record. Refreshing the record on the client after all update events will guarantee the updated record is visible to the client. See your client-specific Advantage help file for details on how to refresh a record.

If an INSTEAD OF trigger exists for a table, AFTER triggers that might also exist on the table are never fired.

An AFTER UPDATE trigger could also be used to slightly modify the new values being written to a table. While not as efficient as an INSTEAD OF trigger (the record update happens twice, instead of once), AFTER triggers can often be written with a much simpler syntax. The example above could be implemented as an AFTER UPDATE trigger:

UPDATE customers SET lastupdate = now() where ID = ( SELECT id FROM \_\_new )

This approach does not require the trigger to be modified each time the table structure changes, as the INSTEAD OF example would. Consider the situation where the "name" column was renamed to "the\_name". The INSTEAD OF trigger above would start failing, because it directly references the column "name", which no longer exists.

CONFLICT triggers are triggers specifically implemented for conflict resolution during replication updates. They are fired when replication detects a record conflict for updated and deleted records; they are not fired for inserted records. Functionally, CONFLICT triggers are very similar to INSTEAD OF triggers. When a replication update is made, CONFLICT triggers are the only type of trigger that will be fired and it is only fired if a conflict is detected.

Like the INSTEAD OF trigger, the CONFLICT trigger replaces the original operation. It is up to the trigger to write the data to the record if desired or to write the information to some kind of log file to keep a history of the conflict.