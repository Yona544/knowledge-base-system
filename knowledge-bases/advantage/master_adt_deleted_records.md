ADT Deleted Records




Advantage Database Server 12  

ADT Deleted Records

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADT Deleted Records  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ADT Deleted Records Advantage Concepts master\_Adt\_deleted\_records Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADT Deleted Records  Advantage Concepts |  |  |  |  |

If a delete record operation is performed on a record in an ADT table, the record is not physically removed from the table. The record is, however, logically removed from the table. Deleted records in an ADT table are not visible to the application. Deleted records cannot be "un-deleted" or "recalled". The space used by records deleted from the table are marked for record re-use. That is, a subsequent append or insert operation will use space marked for re-use before using new space at the end of the table for a new record. Thus, the size of an ADT table will not increase after an append or insert operation if there is space marked for re-use in the table.

If the Pack operation is performed on a table, space marked as available for record re-use will be physically removed from the table.

Note Deleted ADT records may still be recalled if they have not been committed. See the Advantage Client Engine (ACE) APIs AdsRecallRecord or AdsRecallAllRecords in the Advantage Client Engine Help documentation for more information. (Note that each of the Advantage products and their corresponding Help files are installed separately.)