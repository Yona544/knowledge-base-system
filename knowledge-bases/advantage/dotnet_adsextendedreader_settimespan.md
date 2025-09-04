AdsExtendedReader.SetTimeSpan




Advantage Database Server 12  

AdsExtendedReader.SetTimeSpan

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SetTimeSpan  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SetTimeSpan Advantage .NET Data Provider dotnet\_Adsextendedreader\_settimespan Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.SetTimeSpan / Dear Support Staff, |  |
| AdsExtendedReader.SetTimeSpan  Advantage .NET Data Provider |  |  |  |  |

Stores the given TimeSpan value in the specified column.

public void SetTimeSpan( int iCol, TimeSpan value);

Remarks

This method sets the specified zero-based column value to the given TimeSpan value. No conversions are performed. To set a TimeSpan field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.htm)

[AdsDataReader.GetTimeSpan](dotnet_adsdatareader_gettimespan.htm)