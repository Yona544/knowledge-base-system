Transaction-Free Tables




Advantage Database Server 12  

Transaction-Free Tables

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Transaction-Free Tables  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Transaction-Free Tables Advantage Concepts master\_Transaction-Free\_Tables Advantage Concepts > Advantage Functionality > Transaction Processing System (TPS) > Transaction-Free Tables / Dear Support Staff, |  |
| Transaction-Free Tables  Advantage Concepts |  |  |  |  |

There are some cases where it may be desirable to update a table within a transaction, yet have those updates remain outside of the transaction.  While this is possible through the use of a secondary connection for such updates, this is not always feasible (for example when the table is modified in a stored procedure or trigger).  This is where Transaction-Free Tables may be useful.  When a table is defined as a transaction-free table, updates to that table will always be performed outside of any existing transaction scope.  This means that record updates are immediately visible to other users, data locks are released immediately upon record unlock, and a transaction rollback will not roll back updates to that table.

A table can be defined as a transaction-free table at the time of table creation (via the IGNORE TRANSACTIONS clause of a CREATE TABLE statement) or can be modified after table-creation time via AdsSetTableTransactionFree, the sp\_IgnoreTableTransactions system procedure, or the ALTER TABLE statement.

It should be noted that application developers should carefully consider how a given table is used before configuring it to be a transaction-free table.  Only a small subset of tables are appropriate to be defined as transaction-free tables.  There are, however, a few examples of cases where it may be appropriate:

1.  Audit tables.  If triggers (or other mechanisms) are used to produce audit trails when users modify table data, a transaction rollback will also roll back the updates to the audit tables.  Defining these audit tables as transaction-free tables will ensure that they are updated when a user attempts to modify the underlying tables, even if the transaction was rolled back due to permissions or constraint violations.

2.  Key Generating tables.  If a table is used in the generation of key values, where a single record is locked, updated, then unlocked, this table may benefit by being defined as a transaction-free table.  In a traditional transaction, this record would remain locked until the transaction was committed or rolled-back.  This would prevent multiple users from executing this transaction simultaneously, as the lock would cause the entire transaction to become serialized.  By defining such a table as a transaction-free table, multiple users can be permitted to safely execute the transaction.

3.  Log tables. If you use log tables to facilitate debugging it is often helpful to have a log of every operation, even if a transaction is rolled back.  For example, Advantage triggers use implicit transactions. If you are writing to a log table in your trigger, and the trigger encounters an error, Advantage implicitly performs a rollback of all operations performed in the trigger, including your log file messages.  Removing your log tables from transactions can eliminate confusion when analyzing logs.

See Also

[CREATE TABLE](master_create_table.htm)

[ALTER TABLE](master_alter_table.htm)

[sp\_IgnoreTableTransactions](master_sp_ignoretransactions.htm)

[sp\_ModifyTableProperty](master_sp_modifytableproperty.htm)

[AdsSetTableTransactionFree](ace_adssettabletransactionfree.htm)

[Data Locking and Transaction Processing](master_data_locking_and_transaction_processing.htm)