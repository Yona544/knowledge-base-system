AdsExtendedReader.ReadPrevious




Advantage Database Server 12  

AdsExtendedReader.ReadPrevious

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.ReadPrevious  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.ReadPrevious Advantage .NET Data Provider dotnet\_Adsextendedreader\_readprevious Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.ReadPrevious / Dear Support Staff, |  |
| AdsExtendedReader.ReadPrevious  Advantage .NET Data Provider |  |  |  |  |

Moves to the previous record.

public bool ReadPrevious();

Remarks

This returns true if it successfully positioned to the previous row and False if there are no more rows. If you use this method, [AdsDataReader.RecordCache](dotnet_adsdatareader_recordcache.htm) will be changed down to 10 if it is at its original value of 100.

See Also

[AdsDataReader.Read](dotnet_adsdatareader_read.htm)

[AdsDataReader.RecordCache](dotnet_adsdatareader_recordcache.htm)