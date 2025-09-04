Data Update Visibility




Advantage Database Server 12  

Data Update Visibility

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Update Visibility  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Data Update Visibility Advantage Concepts master\_Data\_update\_visibility Advantage Concepts > Advantage ISAM Concepts > Data Update Visibility / Dear Support Staff, |  |
| Data Update Visibility  Advantage Concepts |  |  |  |  |

Visibility of updates to the database occurs on a per record basis. When an application has a lock on a record, the client workstation will have a copy of that record in memory. Due to the record lock, that copy of the record in client memory is guaranteed to be the most recent, and the data in that record can only be changed by the application that maintains the record lock. Updates to one or more individual fields in that record remain visible to only that client application until the write of the entire record is flushed to the Advantage Database Server to be written on the server. While the updates are being made by the client application, the record will still be visible to other users on the network, but they will see the "old" data. Once the Advantage Database Server has written the record, its updated contents are visible to all users. If the client has updated a locked record, a "write record" operation or any movement operation will flush the write of that entire record to the server. Therefore, updates are on a per record basis, and not per field within the record.