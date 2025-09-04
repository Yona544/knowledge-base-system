AdsExtendedReader.RecallRecord




Advantage Database Server 12  

AdsExtendedReader.RecallRecord

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.RecallRecord  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.RecallRecord Advantage .NET Data Provider dotnet\_Adsextendedreader\_recallrecord Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.RecallRecord / Dear Support Staff, |  |
| AdsExtendedReader.RecallRecord  Advantage .NET Data Provider |  |  |  |  |

Restores the current record in a DBF table to normal visibility.

public void RecallRecord();

Remarks

Calling RecallRecord on a deleted record in a DBF table will clear the deleted flag in the first byte of the record.

Note RecallRecord has little effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved nor can they be recalled by a client application. If RecallRecord is called after a call to DeleteRecord and before the record is written, then the record will not be deleted. Once a deleted record has been written either through a call to WriteRecord or implicitly through some record movement, then that record cannot be recalled.

See Also

[DeleteRecord](dotnet_adsextendedreader_deleterecord.htm)

[IsRecordDeleted](dotnet_adsextendedreader_isrecorddeleted.htm)