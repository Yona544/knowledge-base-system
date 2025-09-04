Deleted Records




Advantage Database Server 12  

Deleted Records

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Deleted Records  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - Deleted Records Advantage ODBC Driver odbc\_Deleted\_records Advantage ODBC Driver > Using the Advantage ODBC Driver with SQL > Deleted Records / Dear Support Staff, |  |
| Deleted Records  Advantage ODBC Driver |  |  |  |  |

When a record is deleted in a DBF table, it is not removed from the file, it is simply marked as deleted. These records marked for deletion can be viewed by client applications if the Show Deleted Rows checkbox is marked in the setup utility. Deleted rows can be recovered by a DBF utility or removed from the table by using [sp\_PackTable](master_sp_packtable.htm).

When dealing with Advantage-proprietary ADT tables, deleted records are not visible to applications. The Show Deleted Rows checkbox has no effect when using Advantage-proprietary ADT tables, since deleted records are never visible. sp\_PackTable can be used, however, to remove deleted records from a table.