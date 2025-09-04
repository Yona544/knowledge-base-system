AdsRecordLockingMode




Advantage Database Server 12  

AdsTableOptions.AdsRecordLockingMode

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsRecordLockingMode  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsRecordLockingMode Advantage TDataSet Descendant ade\_Adsrecordlockingmode Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsRecordLockingMode  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Specifies what record locking scheme should be used when editing records in this dataset.

Syntax

TAdsRecordLockingModes = ( lmPessimistic, lmOptimistic );

property AdsRecordLockingMode: TAdsRecordLockingModes read meRecordLockingMode

write meRecordLockingMode default lmPessimistic;

Description

This property can be used to set the record locking mode you would like to use when editing and posting changes to records.

If using pessimistic locking (lmPessimistic), the record in the table will be locked when you put the dataset into edit state. The record will remain locked until you either cancel the update or post your changes.

If using optimistic locking (lmOptimistic), the record in the table will be refreshed when you put the dataset into edit state, but will not be locked. The record will not be locked until you attempt to post your changes. At this point the record will be locked and compared to the record retrieved when the dataset was put into edit state. If some other user has modified the record, an error will be returned. If the record has not been modified, the post operation will continue.

Optimistic locking can be beneficial when lock contention is a concern. For example, if there is a situation where one user might hold a record in edit state for a long period of time (effectively preventing any other users from modifying that record) this might not be desirable. Optimistic locking could be desirable in this situation

Optimistic locking mode can also be used when porting an existing application that was designed to use optimistic record locking.

For performance reasons whenever you are performing any kind of batch operation, where many records will be modified in a short period of time or in a loop, it is best to use pessimistic locking.

The default, and recommended record locking mode is lmPessimistic.