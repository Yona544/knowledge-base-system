7137 Unexpected number of records modified during a replication update




Advantage Database Server 12  

7137 Unexpected number of records modified during a replication update

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7137 Unexpected number of records modified during a replication update  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7137 Unexpected number of records modified during a replication update Advantage Error Guide error\_7137\_unexpected\_number\_of\_records\_modified\_during\_a\_replication\_update Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7137 Unexpected number of records modified during a replication update  Advantage Error Guide |  |  |  |  |

Problem: A replication update resulted in an unexpected number of records updated at the target table. With each update at the source table, there should be one corresponding update at the target.

Solution 1: Verify the identification columns for the table (in the publication definition) uniquely identify the record. If the specified identification columns do not uniquely identify the target record, multiple record updates could occur.

Solution 2: Verify the record to update at the target does exist. The More\_Info field in the ads\_err.adt error log should have information that helps identify the record in question. You may want to check the "Log Data for Failed Replication Updates" in the Advanced tab of the subscription properties dialog in Advantage Data Architect. If this option is chosen, the non-memo data fields of the record will be stored in the error log with the SQL statement that failed.

Solution 3: If the record does not exist at the target and, therefore, cannot be updated successfully, then you can choose the "Ignore Replication Failures" option in the Advanced tab of the subscription properties dialog in Advantage Data Architect. This will cause Advantage to log the 7137 error for the failed update but continue processing the replication queue. Alternatively, you can delete the failed entry from the replication queue. If you are deleting the entry and the failed entry is part of a transaction (TxnID is non-NULL in the replication queue), then you should delete all entries in the transaction.