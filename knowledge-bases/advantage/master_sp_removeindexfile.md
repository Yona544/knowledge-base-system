sp\_RemoveIndexFile




Advantage Database Server 12  

sp\_RemoveIndexFile

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_RemoveIndexFile  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_RemoveIndexFile Advantage SQL Engine master\_Sp\_removeindexfile Advantage SQL > System Procedures > Procedures > sp\_RemoveIndexFile / Dear Support Staff, |  |
| sp\_RemoveIndexFile  Advantage SQL Engine |  |  |  |  |

Disassociates or removes an index file for a database table.

Syntax

sp\_RemoveIndexFile(

TableName,CHARACTER,200,

IndexFileName,CHARACTER,200,

DeleteFile,LOGICAL )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of the table to disassociate the index file. |
| IndexFileName (I) | Base name of the index file not including any directory path. This value should match the index file name from the system.IndexFiles table. |
| DeleteFile (I) | If true, the index will be physically deleted through the operating system. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The table specified by TableName or the index file specified by the IndexFileName cannot be located in the data dictionary. |
| AE\_PERMISSION\_DENIED | The current connected user does not have permission to ALTER the table. |

Remarks

sp\_RemoveIndexFile disassociates or removes an index file associated with a database table. The procedure does not open the table so it is useful for deleting corrupted index file and rebuilding the index from scratch. If the index file is in use by other user, it will not be physically deleted. The [DROP INDEX](master_drop_index.htm) statement is a safer alternative to this procedure.

Example

EXECUTE PROCEDURE sp\_RemoveIndexFile(

Customer Information,

InvoiceDate.ntx,

True );

See Also

[sp\_AddTableToDatabase](master_sp_addtabletodatabase.htm)

[sp\_AddIndexFileToDatabase](master_sp_addindexfiletodatabase.htm)