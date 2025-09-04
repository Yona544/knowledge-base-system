AdsExtendedReader.SetString




Advantage Database Server 12  

AdsExtendedReader.SetString

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SetString  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SetString Advantage .NET Data Provider dotnet\_Adsextendedreader\_setstring Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.SetString / Dear Support Staff, |  |
| AdsExtendedReader.SetString  Advantage .NET Data Provider |  |  |  |  |

Stores the given string value in the specified column.

public void SetString( int iCol, string value );

Remarks

This method sets the specified zero-based column value to the given string value. SetString may be used for character or memo fields. No conversions are performed. To set a string field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.htm)

[AdsDataReader.GetString](dotnet_adsdatareader_getstring.htm)