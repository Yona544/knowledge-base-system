AdsExtendedReader.LogicalRecordNumber




Advantage Database Server 12  

AdsExtendedReader.LogicalRecordNumber

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.LogicalRecordNumber  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.LogicalRecordNumber Advantage .NET Data Provider dotnet\_Adsextendedreader\_logicalrecordnumber Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.LogicalRecordNumber / Dear Support Staff, |  |
| AdsExtendedReader.LogicalRecordNumber  Advantage .NET Data Provider |  |  |  |  |

Retrieves the current logical record number.

public int LogicalRecordNumber{ get; }

Remarks

This property can be used to retrieve a record number that logically takes into account filters ([AdsExtendedReader.Filter](dotnet_adsextendedreader_filter.htm)), ranges ([AdsExtendedReader.SetRange](dotnet_adsextendedreader_setrange.htm)), and deleted records. If an index is active ([AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.htm)), then the value retrieved will be the key number obeying filters and ranges.

Note This property may result in skipping through every record in a table to obtain the count and can be very slow.

See Also

[RecordNumber](dotnet_adsextendedreader_recordnumber.htm)