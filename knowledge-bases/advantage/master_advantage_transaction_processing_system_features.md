Advantage Transaction Processing System Features




Advantage Database Server 12  

Advantage Transaction Processing System Features

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Transaction Processing System Features  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Transaction Processing System Features Advantage Concepts master\_Advantage\_transaction\_processing\_system\_features Advantage Concepts > Advantage Functionality > Transaction Processing System (TPS) > Advantage Transaction Processing System Features / Dear Support Staff, |  |
| Advantage Transaction Processing System Features  Advantage Concepts |  |  |  |  |

Database Stability

The Advantage TPS maintains database stability in the event of workstation or network failure. Should a workstation or the network fail during a transaction, a transaction that is being committed will finish to completion, and an uncommitted transaction will automatically be rolled back. If the file server crashes during a transaction, the Advantage TPS log files are used when the Advantage Database Server is reloaded to return the database to a known state.

Note Advantage only guarantees updates to be written to the operating system. The operating system has the responsibility to physically write information to the servers hard disk.

Data Hiding (Read Committed Isolation Level)

The Advantage TPS uses the Read Committed Isolation Level to build robustness into database applications by only allowing visibility of committed data. While updates are being made within a transaction, the Advantage TPS hides those updates from other users until that data is committed. The uncommitted data is visible only to the application performing the transaction. The other applications view the data as it was before the transaction began. If the transaction is rolled back, the uncommitted data is never seen by any users other than the one who was performing the transaction. If the transaction is committed, the updated data becomes visible to all users at one time.

Recovery from System Failures

Automatic recovery of your database to a known state after a system failure is a key feature of the Advantage TPS. System failures in this context are server failures, such as operating system read or write errors. How the Advantage TPS handles system failures depends on what phase the transaction was in when the system failure occurred.

A transaction can be in one of three phases: the Build Phase, the Commit Phase, or the Rollback Phase. The Build Phase is active as insert, update, and delete operations are being issued by the application. These operations are logged to the transaction log file by the Advantage TPS during this phase. The Commit Phase occurs after the Advantage application issues a commit transaction statement. This signals the Advantage TPS to begin writing the database updates that are stored in the transaction log file to the tables and index files. The Rollback Phase occurs after the Advantage application issues a rollback transaction statement. This signals the Advantage TPS to abort all database updates that are stored in the transaction log file. The database is left exactly as it was before the transaction began.

If a system failure occurs during the Build Phase, the Advantage TPS aborts only the insert, update, or delete operation that was in progress. The database is left as it was before the individual operation occurred and the transaction remains in the Build Phase. An error is returned to the application indicating that the insert, update, or delete operation failed.

If a system failure occurs during the Commit Phase, the Advantage TPS puts the transaction into the Rollback Phase. The entire transaction is aborted (rolled back). The database is left as it was before the transaction began and the transaction is complete. An error is returned to the application indicating the transaction was rolled back.

If a system failure occurs during the Rollback Phase, a failed transaction results. The tables and index files associated with the transaction will be left in a temporarily unstable state. An error is returned to the application indicating the transaction failed. The application needs to recognize this error and attempt a failed transaction recovery. While the Advantage Database Server is loaded/started, a failed transaction can be recovered from by calling the applicable Advantage client "failed transaction recovery" or "TPS cleanup" API. After the failed transaction recovery is completed, the database will be as it was before the transaction began. See your Advantage client-specific documentation for more information about the failed transaction recovery APIs.

Note In order for a failed transaction recovery to be successful, no other applications can have the tables and index files open that are involved with the transaction.

Recovery from Server Crashes

Should a server crash due to a power outage, exception, or other critical error while one or more applications are in the midst of a transaction, a failed transaction(s) will result. The tables and index files associated with the transaction(s) will be left in a temporarily unstable state. The Advantage TPS can recover from the failed transactions and return the tables and index files to a known state. After bringing the file server back up, reload/restart the Advantage Database Server. Loading/starting the Advantage Database Server automatically triggers failed transaction recovery. Any transactions that were in the Build Phase when the server crashed will be rolled back. Any transactions that were in the Commit Phase will continue with the commit. Any transactions that were in the Rollback Phase will continue with the rollback.

Always view the Advantage Database Server error log, ADS\_ERR.ADT or ADS\_ERR.DBF, to determine if the Failed Transaction Recovery was successful. If a Failed Transaction Recovery error is encountered, contact Advantage [Technical Support](master_technical_support_u_s__and_canada.htm). It is recommended that periodic server backups be a part of any disaster recovery plan.

Nested Transactions

Transactions can be nested within other transactions. When you nest begin and commit transaction operations, the outermost pair actually begin and commit the transaction. The inner pairs are used to keep track of the nesting level. The Advantage Database Server does not commit the transaction until the commit transaction that matches the outermost begin transaction is issued. Normally, transaction nesting occurs as stored procedures contain begin and commit operation pairs. See Nested Transaction for more details.