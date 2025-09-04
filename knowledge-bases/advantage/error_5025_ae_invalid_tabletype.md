5025 AE\_INVALID\_TABLETYPE




Advantage Database Server 12  

5025 AE\_INVALID\_TABLETYPE

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5025 AE\_INVALID\_TABLETYPE  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5025 AE\_INVALID\_TABLETYPE Advantage Error Guide error\_5025\_ae\_invalid\_tabletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5025 AE\_INVALID\_TABLETYPE  Advantage Error Guide |  |  |  |  |

An invalid table type was specified. Valid choices are ADS\_CDX, ADS\_NTX, ADS\_VFP or ADS\_ADT. The table type must support the memo file type to be opened, if applicable. The ADS\_ADT table type supports ADT tables, ADI indexes, and ADM memos. The ADS\_CDX and ADS\_VFP table types support DBF tables, CDX and IDX indexes, and FPT memos. The ADS\_NTX table type supports DBF tables, NTX indexes, and DBT memos.

The ADS\_VFP table type is a superset of the ADS\_CDX type. If a DBF table contains field types such as Timestamp (DateTime), Currency (Money), VarBinary, etc., you must use table type ADS\_VFP to open it.