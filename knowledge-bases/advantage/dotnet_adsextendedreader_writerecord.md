AdsExtendedReader.WriteRecord




Advantage Database Server 12  

AdsExtendedReader.WriteRecord

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.WriteRecord  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.WriteRecord Advantage .NET Data Provider dotnet\_Adsextendedreader\_writerecord Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.WriteRecord / Dear Support Staff, |  |
| AdsExtendedReader.WriteRecord  Advantage .NET Data Provider |  |  |  |  |

Writes any changes in the current record.

public void WriteRecord();

Remarks

WriteRecord flushes any data changes to the Advantage server. If an implicit lock is held on the record, calling this function will release it.