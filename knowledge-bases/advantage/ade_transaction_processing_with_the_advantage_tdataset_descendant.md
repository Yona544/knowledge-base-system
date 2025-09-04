Transaction Processing with the Advantage TDataSet Descendant




Advantage Database Server 12  

Transaction Processing with the Advantage TDataSet Descendant

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Transaction Processing with the Advantage TDataSet Descendant  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Transaction Processing with the Advantage TDataSet Descendant Advantage TDataSet Descendant ade\_Transaction\_processing\_with\_the\_advantage\_tdataset\_descendant Advantage TDataSet Descendant > Developing and Distributing Applications > Transaction Processing with the Advantage TDataSet Descendant / Dear Support Staff, |  |
| Transaction Processing with the Advantage TDataSet Descendant  Advantage TDataSet Descendant |  |  |  |  |

Advantage Transaction Processing is aligned with the existing Delphi scheme as much as possible.

The Advantage TAdsConnection component has encapsulated Advantage Transaction Processing in the Advantage TDataSet Descendant solution. Use the TAdsConnection component to perform transaction processing with the Advantage TDataSet Descendant solution. The TAdsConnection methods and property applicable to transaction processing are:

[TAdsConnection.BeginTransaction](ade_begintransaction.htm)

Begins a transaction for all tables associated with the instance of TAdsConnection.

[TAdsConnection.Rollback](ade_rollback.htm)

Aborts a transaction. Any updates, deletes, and inserts issued since the transaction began will be aborted.

[TAdsConnection.Commit](ade_commit.htm)

Commits the changes since the transaction began.

[TAdsConnection.TransactionActive](ade_transactionactive.htm)

Boolean property to indicate if a transaction is active.

TAdsConnection.TransactionCount

Returns the current transaction nesting level.