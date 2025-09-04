Advantage TPS Error Conditions




Advantage Database Server 12  

Advantage TPS Error Conditions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage TPS Error Conditions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage TPS Error Conditions Advantage Concepts master\_Advantage\_tps\_error\_conditions Advantage Concepts > Advantage Functionality > Transaction Processing System (TPS) > Advantage TPS Error Conditions / Dear Support Staff, |  |
| Advantage TPS Error Conditions  Advantage Concepts |  |  |  |  |

A few Advantage functions are illegal and will generate errors if used during a transaction. These functions, if allowed during a transaction, would prevent the transaction from functioning properly. To prevent using these functions in a transaction, Advantage TPS returns an error if they are encountered. Each illegal operation is described below.

Pack and Zap (EmptyTable)

Packing or zapping a file during a transaction is illegal. If a pack or zap operation are attempted during a transaction, a 5063, "The command is illegal within a transaction" error is generated. Packing and zapping a table are illegal during a transaction because Advantage TPS cannot "unpack" or "unzap" a file in the event of a transaction rollback.

Reindex

Reindexing an index file during a transaction is illegal. If a reindex is attempted during a transaction, a 5063, "The command is illegal within a transaction" error is generated. A reindex is illegal during a transaction because Advantage TPS may have multiple index keys referencing a single record during a transaction for data visibility purposes. A reindex of the index would disable this ability.

Delete a CDX or ADI Index (Tag)

Deleting an index order (tag) from a compound index file is illegal during a transaction. If an attempt is made to delete an index (tag) during a transaction, a 5063, "A command is illegal within a transaction," error is generated. Deleting a CDX or ADI index (tag) is illegal during a transaction because Advantage TPS cannot "undelete" a tag in the event of a transaction rollback.

Application Termination During a Transaction

If an application terminates, whether normally or abnormally, any active transactions will be rolled back.