AdsDataReader.Read




Advantage Database Server 12  

AdsDataReader.Read

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.Read  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.Read Advantage .NET Data Provider dotnet\_Adsdatareader\_read Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.Read / Dear Support Staff, |  |
| AdsDataReader.Read  Advantage .NET Data Provider |  |  |  |  |

Advances the AdsDataReader to the next record.

public bool Read();

Remarks

Read returns True if it successfully positioned to the next row and False if there are no more rows. The default position of the AdsDataReader is prior to the first record. Therefore, you must call Read to begin accessing any data.

See Also

[AdsCommand.ExecuteReader](dotnet_adscommand_executereader.htm)

[RecordCache](dotnet_adsdatareader_recordcache.htm)