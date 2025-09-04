AdsExtendedReader.GotoBOF




Advantage Database Server 12  

AdsExtendedReader.GotoBOF

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.GotoBOF  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.GotoBOF Advantage .NET Data Provider dotnet\_Adsextendedreader\_gotobof Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.GotoBOF / Dear Support Staff, |  |
| AdsExtendedReader.GotoBOF  Advantage .NET Data Provider |  |  |  |  |

Sets the table position to BOF (beginning of file), which is prior to the first record.

public void GotoBOF();

Remarks

This positions the reader prior to the first record in the record set. A call to AdsDataReader.Read after a call to GotoBOF will position the reader on the first record. This simulates the situation of a newly opened reader. It allows code such as the following to work as expected:

reader.GotoBOF();

while ( reader.Read() )

{

// do stuff

}

See Also

[AdsDataReader.Read](dotnet_adsdatareader_read.htm)

[GotoTop](dotnet_adsextendedreader_gototop.htm)

[BOF](dotnet_adsextendedreader_bof.htm)