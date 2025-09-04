Updating Data in Rowsets




Advantage Database Server 12  

Updating Data in Rowsets

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Updating Data in Rowsets  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Updating Data in Rowsets Advantage OLE DB Provider (for ADO) oledb\_Updating\_data\_in\_rowsets Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Rowsets > Updating Data in Rowsets / Dear Support Staff, |  |
| Updating Data in Rowsets  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider updates the Advantage Database Server data when a consumer updates a modifiable rowset containing that data. A modifiable rowset is created when the consumer requests support for either the IRowsetChange or IRowsetUpdate interface.

Immediate and Delayed Update Modes

In immediate update mode, each call to IRowsetChange::SetData results in a round-trip to the Advantage Database Server. If the consumer makes multiple changes to a single row, it is more efficient to submit all changes with a single SetData call.

In delayed update mode, a round-trip is made to the Advantage Database Server for each row indicated in the cRows and rghRows parameters of IRowsetUpdate::Update.

In either mode, a round-trip represents a distinct transaction when no transaction object is open for the rowset.

When using IRowsetUpdate::Update, the Advantage OLE DB Provider attempts to process each indicated row. An error occurring due to invalid data, length, or status values for any row does not stop the Advantage OLE DB Provider processing. All or none of the other rows participating in the update may be modified. The consumer must check the returned prgRowStatus array to determine failure for any specific row when the Advantage OLE DB Provider returns DB\_S\_ERRORSOCCURRED.

A consumer should not assume that rows are processed in any specific order. If a consumer requires ordered processing of data modification over more than a single row, the consumer should establish that order in application logic and open a transaction to enclose the process.

Refreshing Rows

The Advantage OLE DB Provider supports IRowsetRefresh to synchronize rows in the rowset with those in the data store.