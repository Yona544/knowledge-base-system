Locking Type




Advantage Database Server 12  

Locking Type

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Locking Type |  |  | Feedback on: Advantage Database Server 12 - Locking Type odbc\_Locking\_type Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Locking Type |  |  |  |  |

Record or File locking may be specified as the default when handling the database files. When locks are established, to update data for example, either a record can be locked in the database file or the entire file may be locked.

Establishing the Locking setting is largely a performance issue. In most cases, record locking provides good performance while still maintaining concurrency control. However, if a large number of records are being updated in one file, file locks allow the updates to be performed faster.