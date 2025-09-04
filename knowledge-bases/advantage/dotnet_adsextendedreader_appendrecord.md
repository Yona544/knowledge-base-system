AdsExtendedReader.AppendRecord




Advantage Database Server 12  

AdsExtendedReader.AppendRecord

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.AppendRecord  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.AppendRecord Advantage .NET Data Provider dotnet\_Adsextendedreader\_appendrecord Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.AppendRecord / Dear Support Staff, |  |
| AdsExtendedReader.AppendRecord  Advantage .NET Data Provider |  |  |  |  |

Appends an empty record to the end of the table.

public void AppendRecord();

Remarks

AppendRecord appends a blank record to the end of the table, locks the record, and positions the table to the new record. Changes are written when the user moves off of the appended record or calls WriteRecord. Transactions have some affect on appending records; see [Advantage Transaction Processing](master_advantage_transaction_processing_system_overview.htm) for more information on appends during transactions.

Note With ADT tables, Advantage implements a record re-use algorithm that recycles records that have been deleted (DeleteRecord). This means that the newly appended record may not actually be at the end of the table. An application should not make any assumptions about the new record number.

See Also

[DeleteRecord](dotnet_adsextendedreader_deleterecord.htm)

[RecordNumber](dotnet_adsextendedreader_recordnumber.htm)