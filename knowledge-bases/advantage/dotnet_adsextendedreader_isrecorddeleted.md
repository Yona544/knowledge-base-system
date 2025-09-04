AdsExtendedReader.IsRecordDeleted




Advantage Database Server 12  

AdsExtendedReader.IsRecordDeleted

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.IsRecordDeleted  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.IsRecordDeleted Advantage .NET Data Provider dotnet\_Adsextendedreader\_isrecorddeleted Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.IsRecordDeleted / Dear Support Staff, |  |
| AdsExtendedReader.IsRecordDeleted  Advantage .NET Data Provider |  |  |  |  |

Tests the deleted status of the current record.

public bool IsRecordDeleted();

 

Remarks

The first byte of every record in a DBF table is reserved for use as a deleted byte. This byte signals whether the record is deleted. This method returns true if the record is marked as deleted.

Note IsRecordDeleted will generally return false for Advantage proprietary ADT tables. Records that are deleted in ADT tables are permanently deleted and can never be retrieved by a client application once they have been written. It is possible to call IsRecordDeleted just after calling DeleteRecord and before the record is written. This function will return true in that case.

See Also

[DeleteRecord](dotnet_adsextendedreader_deleterecord.htm)

[RecallRecord](dotnet_adsextendedreader_recallrecord.htm)

[PackTable](dotnet_adsextendedreader_packtable.htm)