sp\_PackTable




Advantage Database Server 12  

sp\_PackTable

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_PackTable  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_PackTable Advantage SQL Engine master\_Sp\_packtable Advantage SQL > System Procedures > Procedures > sp\_PackTable / Dear Support Staff, |  |
| sp\_PackTable  Advantage SQL Engine |  |  |  |  |

Removes all deleted records from a table and re-indexes it.

Syntax

sp\_PackTable( TableName,CHARACTER,515 )

 

sp\_PackTable( TableName,CHARACTER,515,

             MemoBlockSize,INTEGER )

 

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name and/or path of a table to pack. |
| MemoBlockSize (I) | Optional memo block size. If this is not provided or if the value is 0, the memo block size will not be changed by the pack operation. |

Remarks

sp\_PackTable performs a pack of a table which removes all deleted records from the table. Internal fragmentation in memo files will also be eliminated. It then re-indexes the table. This operation requires exclusive access to the table, no process can have this table open when calling this procedure. Only auto-open indexes will be re-indexed. sp\_PackTable is illegal in a transaction. The TableName parameter must specify the table name of a dictionary bound table, or the table path of a [free table](javascript:hhpopuplink.TextPopup(popid_1535016085X,FontFace,-1,-1,-1,-1)).

See Also

[AdsPackTable](ace_adspacktable.htm)

[sp\_PackTableOnline](master_sp_packtableonline.htm)

[sp\_ZapTable](master_sp_zaptable.htm)