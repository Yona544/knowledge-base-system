AdsExtendedReader.RecordNumber




Advantage Database Server 12  

AdsExtendedReader.RecordNumber

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.RecordNumber  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.RecordNumber Advantage .NET Data Provider dotnet\_Adsextendedreader\_recordnumber Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.RecordNumber / Dear Support Staff, |  |
| AdsExtendedReader.RecordNumber  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the current record number.

public int RecordNumber{ get; set; }

Remarks

Each physical record in a table has a record number. The first physical record is number 1. All records, even deleted ones (in DBF tables), have record numbers. The only way to change record numbers in a table is to perform a [PackTable](dotnet_adsextendedreader_packtable.htm).

RecordNumber ignores filters, indexes, and scopes. It sets the physical record number even if an index is active. If set to zero or a number greater than the total number of records, the client will be unpositioned (EOF and BOF will be set) and the current record number will be set to 0.

Note If setting the RecordNumber property and using the AdsExtendedReader.Read method, the Read method will skip FROM the record number that was set using the RecordNumber property, which means values read will be from the next record in the dataset, not the record explicitly set via RecordNumber.

See Also

[GetBookmark](dotnet_adsextendedreader_getbookmark.htm)

[GotoBookmark](dotnet_adsextendedreader_gotobookmark.htm)

[LogicalRecordNumber](dotnet_adsextendedreader_logicalrecordnumber.htm)