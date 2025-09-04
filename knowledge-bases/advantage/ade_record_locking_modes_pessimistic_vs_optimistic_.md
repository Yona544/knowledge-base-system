Record Locking Modes (pessimistic vs. optimistic)




Advantage Database Server 12  

Record Locking Modes (pessimistic vs. optimistic)

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Record Locking Modes (pessimistic vs. optimistic)  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Record Locking Modes (pessimistic vs. optimistic) Advantage TDataSet Descendant ade\_Record\_locking\_modes\_pessimistic\_vs\_optimistic\_ Advantage TDataSet Descendant > Converting Existing Delphi Applications > Record Locking Modes (pessimistic vs. optimistic) / Dear Support Staff, |  |
| Record Locking Modes (pessimistic vs. optimistic)  Advantage TDataSet Descendant |  |  |  |  |

If you are converting an application that previously used a different database, and that database used optimistic locking, you may want to configure your Advantage-enabled application to use optimistic locking as well.

When using pessimistic locking, records in a table will be locked when you put the dataset into edit state. The records will remain locked until you either cancel the update or post your changes.

When using optimistic locking, records in a table will be refreshed when you put the dataset into edit state, but will not be locked. Records will not be locked until you attempt to post your changes. At this point the record in question will be locked and compared to the record retrieved when the dataset was put into edit state. If some other user has modified the record, an error will be returned. If the record has not been modified, the post operation will continue.

Note that often even if your application was written using a database that supported optimistic record locking, you do not need to use optimistic locking with Advantage. Many applications will run as expected even though they are now using pessimistic record locking (which is the default and recommended Advantage record locking mode).

The [AdsTableOptions.AdsRecordLockingMode](ade_adsrecordlockingmode.htm) property can be used to specify what record locking mode you would like the dataset to use.