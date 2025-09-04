Advantage Error Log and Replication




Advantage Database Server 12  

Advantage Error Log and Replication

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Error Log and Replication  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Error Log and Replication Advantage Concepts master\_Advantage\_error\_log\_and\_replication Advantage Concepts > Advantage Functionality > Replication > Advantage Error Log and Replication / Dear Support Staff, |  |
| Advantage Error Log and Replication  Advantage Concepts |  |  |  |  |

Replication errors and warnings are logged to the Advantage error log. Beginning with version 8.0, the default error log is an ADT table (ads\_err.adt). If Advantage is not able to open or write to ads\_err.adt, the errors will be logged to ads\_err.dbf.

Replication errors and warnings have error class 7600. The ads\_err.adt error log has a memo field named More\_Info that will contain the bulk of the information for replication errors. For example, it will contain the SQL statement for failed updates.

Beginning with v10.10.0.6, some of the same information that is in the error log is also written directly to the replication queue itself when possible. If the queue has been updated to use this feature, you can open the queue table and read the error information in the fields titled ErrorCode, ErrorInfo, and ErrorInfo2. This may be simpler than searching through the error log for the failure. If the replication queue was created with an earlier version of Advantage, it will not have these fields. It is possible to delete the queue table from the dictionary (e.g., right click on the table in Advantage Data Architect), and it will then be created again with the new fields the next time it is used. Be sure to verify that the queue is empty prior to deleting it, otherwise any pending updates contained in the queue will be lost.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)