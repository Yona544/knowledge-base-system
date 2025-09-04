AX\_Transaction()




Advantage Database Server 12  

AX\_Transaction()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_Transaction()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_Transaction() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_transaction Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_Transaction() / Dear Support Staff, |  |
| AX\_Transaction()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Begins, commits, rolls back, or shows the state of a transaction

Syntax

AX\_Transaction( <nTransactionType> ) -> logical

|  |  |
| --- | --- |
| <nTransactionType> | Specifies the transaction command to be carried out. The constants used with Advantage are described in the Constants section below. |

Returns

True if the command was successful, False if not.

Constants

AX\_BEGIN\_TRANSACTION

Marks the beginning of an Advantage TPS transaction. From this point on in your application until an AX\_COMMIT\_TRANSACTION or AX\_ROLLBACK\_TRANSACTION, every append and replace command issued before a corresponding commit or rollback will be considered one transaction.

Once you begin an Advantage transaction, any updates made to the database are tracked in a transaction log file. Other users sharing the same database files will not see any changes to the database until the transaction is committed. When the transaction is committed, the changes are written to the database files and indexes.

AX\_COMMIT\_TRANSACTION

Indicates the end of a transaction and signifies all updates issued during the transaction be written to the database. These updates are made visible to all other users at this time.

AX\_ROLLBACK\_TRANSACTION

Indicates the end of a transaction and signifies all updates issued during the transaction be aborted. All of the data altered since the beginning of the transaction is restored to its previous value. The pending updates are rolled back and cannot be recovered.

AX\_ISACTIVE\_TRANSACTION

Indicates if the user is currently in a transaction (.T.) or not (.F.).

Note A call to AX\_Transaction( AX\_BEGIN\_TRANSACTION ) begins a transaction on all existing Advantage connections that do not already have transactions active. If you wish to begin a transaction on a specific Advantage connection only, you can either call the Advantage Client Engine AdsBeginTransaction API or modify the AX\_Transaction code in the DBFAXS.AEF file to accept an Advantage connection handle as a parameter.

Description

This function is the main function for the Advantage TPS. All the transaction command statements are issued from this function.

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.htm) for code sample for the AxDBServer class.

|  |
| --- |
| oDB := AxDBServer{ "TEST", .F., .F., "DBFNTXAX" } |
|  |
| ? oDB:AX\_Transaction()  // Returns .F. |
|  |
| oDB:AX\_Transaction( AX\_BEGIN\_TRANSACTION ) |
| ? oDB:AX\_Transaction() // Returns .T. |
| oDB:Append() |
| oDB:AX\_Transaction( AX\_COMMIT\_TRANSACTION ) |
|  |
| ? oDB:AX\_Transaction()  // Returns .F. |

Procedural Example

|  |
| --- |
| USE test VIA "DBFNTXAX" |
|  |
| ? AX\_Transaction()  // Returns .F. |
|  |
| AX\_Transaction( AX\_BEGIN\_TRANSACTION ) |
| ? AX\_Transaction() // Returns .T. |
| DBAppend() |
| AX\_Transaction( AX\_COMMIT\_TRANSACTION ) |
|  |
| ? AX\_Transaction()  // Returns .F. |