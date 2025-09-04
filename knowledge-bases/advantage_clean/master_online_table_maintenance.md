---
title: Master Online Table Maintenance
slug: master_online_table_maintenance
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_online_table_maintenance.htm
source: Advantage CHM
tags:
  - master
checksum: 853ede59e40fb257b5cb6687d1b8ac2bd5f75915
---

# Master Online Table Maintenance

Online Table Maintenance

Online Table Maintenance

Advantage Database Server

| Online Table Maintenance  Advantage Database Server |  |  |  |  |

Online Pack, Reindex, Create Index and ALTER TABLE

Online pack is a version of the regular pack functionality that is allowed on tables that are currently in use by other users.  The goal of online pack is the same as the regular pack: remove deleted records from the table, rebuild all indexes on the table, and rebuild the memo file to reduce internal fragmentation.

Online reindex is a version of the regular reindex functionality that is allowed on tables that are currently in use by other users.  The goal of online reindex is the same as regular reindex:  rebuild the indexes opened on a table.

Online Create Index is a version of the regular create index functionality that is allowed on tables that are currently in use by other users.  This allows you to add indexes on the fly to optimize query performance or provide additional table sorting options.  Indexes created using the online functionality are identical to regular indexes and logically correct upon creation.

Online ALTER TABLE is a version of the regular ALTER TABLE functionality that is allowed on tables that are currently in use by other users.  The goal of online ALTER TABLE is the same as regular ALTER TABLE: alter the structure of a table including add, remove, or modify columns.  Indexes and memo files are rebuilt during the process.

Because these online operations allow other users access to the table during the operation, there are some limitations and behavioral differences compared to the regular functionality.  This page lists those differences and how an application should expect the online version to work.  See the specific help pages for [sp\_PackTableOnline](master_sp_packtableonline.md), [sp\_ReindexOnline](master_sp_reindexonline.md), [CREATE INDEX](master_create_index.md), and [ALTER TABLE](master_alter_table.md) for information about how to initiate the online operations.

Limitations

Online pack, reindex, create index, and ALTER TABLE are only supported on remote or internet server connections and tables opened with proprietary locking.

Stages of the Online Operations

Online pack includes three stages of processing: setup, packing, and transitioning (final stage).  In the setup stage the new table and indexes are created and prepared for the packing.  In the packing stage, the new table and indexes are populated with the existing data of the original table.  Updates made to the table and indexes during the pack are also applied to the new table and indexes.  The transition stage is where the final steps are taken to transition users from the original table to the new table.  During the entire online pack process users are allowed to update the table as they normally would.

Online reindex includes three stages of processing: setup, reindexing, and the final stage.  During the setup stage new indexes are prepared for building.  During the reindexing stage the new indexes are built.  During the final stage updates to the table during the build are applied to the new indexes and finally the new and old indexes are swapped.  There is no real transition with online reindex, but the final stage cannot begin until there are no active record locks on the table.  Once the final stage is complete the operation is done and users of the table don't need to do anything special to begin using the new indexes.

Online ALTER TABLE performs the first two stages similar to online pack and reindex.  However the third and final stage may or may not include a transition depending on what kind of changes to the table structure are performed.  For most simple changes such as adding or removing a field, the final stage of the alter will complete once all locks held by other users on table are released and any replication queues for the table are empty.  There would be no real transition performed and existing users of the table will be able to continue working on the table without delay.  This is called a No-Transition Alter.  One side effect of a No-Transition Alter is that deleted records are kept in the new table.  For some more complex changes to the table structure, a transition during the final stage where all users are required to close the table is required.  This is called the Transition Alter.  The more complex changes that require a Transition Alter are:

- Modify a field that is included in an index key expression

- Any change to a table that has an AES encrypted index

- Converting a blob field to a non-blob field or a blob field to a different type of blob field (example: Char to Memo or Memo to NMemo)

- Changing the memo block size of a memo file

- Changing the transaction-free setting of a table

It is important to understand that a Transition Alter will not complete until all users of the table close the table and any replication queues for the table are emptied during the final stage.  While this is more disruptive than a No-Transition Alter, it still provides a benefit over a non-online alter by minimizing the time that the table must be closed.  The majority of the time required for an alter is spent creating and populating the table with the new structure.  With online alter that work is done while the table is open shared and available to other users.  So even though the final stage of a Transition Alter requires all users to close the table, the work done in that stage is minimal and the table is again available very quickly.  The result is that an alter of a large table might have required hours of downtime previously, now only requires seconds of downtime.

Transitioning to the New Table During Online Pack

Clients cannot transition to the new table until all locks on the table are released.  The pack operation must wait until all updates to the table are committed before the transition stage can begin.

In order for a user to transition to the new table of an online pack, they must make a call to the server and reposition their record pointer.  The server calls that can transition a user are Goto, GoTop, GoBottom, Skip, Seek, SetFilter, Append, SetRelativeKeyPosition, GoScopeEnd, GetFilteredRecordCount, GetRecordCount, and CloseTable.  The online pack operation will not fully complete until all users of the table have transitioned.  Note that the system procedure sp\_PackTableOnline will return from the server when the transition stage begins.  The entire operation isn't complete until all users transition to the new table, but the system procedure doesn't need to wait for that to happen before returning.

Using The Final Stage Event Notification

At the start of the final stage of an online pack, create index or reindex operation, an event will be signaled.  For online pack the event name is \_\_OPFinalStage\_tablename where tablename is the name of the table being packed.  For example if you were packing customers.adt the event name would be \_\_OPFinalStage\_customers.  Similarly, an online reindex will signal the event name \_\_ORFinalStage\_tablename where tablename is the name of the table being reindexed.

For an online create index operation the event name would be \_\_OCIFinalStage\_tablename where tablename is the name of the table for which the index belongs.  The online create index event will be signaled at the end of the index build process when the new index is available for use.  An online create index operation does not require any action from users of the table in order for it to complete.  The final stage event notification is only meant to be an indication that a new index is available for the table.  Applications will need to close and re-open the table to begin using the new index.  The SQL engine will begin using the new index immediately for optimization as it opens tables with each new query.  Note that the Advantage server will maintain the new index and keep it logically correct whether client applications know about the new index or not.

For an online alter table operation the event name would be \_\_OAFinalStage\_tablename where tablename is the name of the table being altered.  The online alter event will be signaled at the beginning of the final stage as well as once a minute while the operation is in the final stage.  This is different than online pack and reindex because online alter cannot finish until all users close the table being altered.

The purpose of the online operation event is to provide other users a notification that they should take action to help the online operation complete.  Users with the table open during a pack should make a server call to transition to the new table (see transitioning above).  Users with the table open during an online alter should close the table in order for the operation to finish.

The online operation event must be created and waited on by the client.  The server will only signal the event.  If the event doesn't exist, nothing will happen.  An application that can react to online operations should create the appropriate event and periodically or indefinitely wait on the event to see if an online operation is waiting to complete.

For example, this call will create an online pack event for table customers:

EXECUTE PROCEDURE [sp\_CreateEvent](master_sp_createevent.md)( '\_\_OPFinalStage\_customers', 0 );

This call will check to see if the event was signaled.  If the EventCount value returned is greater than zero then an online pack has occurred since the last time the event was checked:

EXECUTE PROCEDURE [sp\_WaitForEvent](master_sp_waitforevent.md)( '\_\_OPFinalStage\_customers', 0, 0, 0 );

ROWID During an Online Pack

Because during a pack record numbers can be changing, ROWID values can also change or become invalid.  Using a ROWID value for a table that is being packed can produce unexpected results including positioning on the wrong record or returning an invalid ROWID error.  To help prevent this unexpected behavior, an error (7215) will be returned if Advantage detects a query using a ROWID value for a table being packed online.  Advantage cannot detect all situations where a ROWID value is invalid however.  Care should be taken not to use invalid ROWID values when using online pack.

Modifying Deleted Records During Online Pack

If during an online pack a user modifies a deleted record, that record will be added to the new table.  However the record number (position of the record in the table) cannot be guaranteed.  Depending on when the update occurs during the pack it may be in the original position or it may be at the end of the new table.  Clients need to understand that the positions of records in the table will likely be changing during an online pack.  Unless the update changes the deleted status of the record, the record will be added to the new table as a deleted record.

Refresh Encrypted Records Before Transition

Invalid data may be returned if a client does a refresh of the current record (AdsRefreshRecord) during the final stage of an online pack before transitioning.  To avoid this the client should make a call to the server that will transition them to the new table before refreshing the record.

Online ALTER TABLE and Field Constraints

The [ALTER TABLE](master_alter_table.md) syntax allows adding or dropping field constraints including default field values and NOT NULL flags.  With a non-online alter these field properties are set after the new table is created and all the existing data is copied into it.  With online alter, default field values and NOT NULL flags for added fields are set before the new table is populated.  The result is that any added fields that have a default value are initialized to that default value and any added field that has a NOT NULL constraint will need a default value other than NULL.  Other field constraints including minimum or maximum values are still set after the data copy is complete and won't be enforced until after the alter is done.  Note that with online alter, default field values and NOT NULL flags for new fields will be enforced even for users that have the table open and are not aware of the new field.  These constraints will be enforced by the server until the client closes and re-opens the table at which point the client will begin enforcing them.  Although default field values and NOT NULL flags are only enforced for dictionary bound tables, with online alter these constraints will be applied to new free tables as well for added fields when the new table is populated with existing data.  However once the alter is complete, the constraints will not be enforced on free tables.
