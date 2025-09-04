sp\_ZapTable




Advantage Database Server 12  

sp\_ZapTable

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ZapTable  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ZapTable Advantage SQL Engine master\_Sp\_zaptable Advantage SQL > System Procedures > Procedures > sp\_ZapTable / Dear Support Staff, |  |
| sp\_ZapTable  Advantage SQL Engine |  |  |  |  |

Removes all data from a table and re-indexes it.

Syntax

sp\_ZapTable( TableName,CHARACTER,515 )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name and/or path of a table to zap. |

Remarks

sp\_ZapTable performs a zap of a table which removes all records from the table and all data from the memo file then re-indexes the table. This operation requires exclusive access to the table; no process can have this table open when calling this procedure. Only auto-open indexes will be re-indexed. sp\_ZapTable is illegal in a transaction. The TableName parameter must specify the table name of a dictionary bound table, or the table path of a [free table](javascript:hhpopuplink.TextPopup(popid_1535016085X,FontFace,-1,-1,-1,-1)).

See Also

[AdsZapTable](ace_adszaptable.htm)

[sp\_PackTable](master_sp_packtable.htm)