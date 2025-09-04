Deleted Records are Invisible and Automatically Reused




Advantage Database Server 12  

Deleted Records are Invisible and Automatically Reused

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Deleted Records are Invisible and Automatically Reused  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Deleted Records are Invisible and Automatically Reused Advantage Concepts master\_Deleted\_records\_are\_invisible\_and\_automatically\_reused Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > Deleted Records are Invisible and Automatically Reused / Dear Support Staff, |  |
| Deleted Records are Invisible and Automatically Reused  Advantage Concepts |  |  |  |  |

If a delete record operation is performed on a record in an ADT table, the record is not physically removed from the table. The record is, however, logically removed from the table. Deleted records in an ADT table are not visible to the application. Deleted records cannot be "undeleted" or "recalled". The space used by records deleted from the table are marked for record reuse. That is, a subsequent append or insert operation will use space marked for reuse before using new space at the end of the table for a new record. Thus, the size of an ADT table will not increase after an append or insert operation if there is space marked for reuse in the table.

If you desire the delete record operation to delete records such that they are no longer visible to any application and you do not want space used by deleted records to bloat the size of your tables (as can happen with Xbase tables), you may want to use the [Advantage Proprietary Format](master_advantage_proprietary_format.htm).