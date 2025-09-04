AdsExtendedReader.SetDecimal




Advantage Database Server 12  

AdsExtendedReader.SetDecimal

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SetDecimal  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SetDecimal Advantage .NET Data Provider dotnet\_Adsextendedreader\_setdecimal Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.SetDecimal / Dear Support Staff, |  |
| AdsExtendedReader.SetDecimal  Advantage .NET Data Provider |  |  |  |  |

Stores the given Decimal value in the specified column.

public void SetDecimal( int iCol, Decimal value );

Remarks

This method sets the specified zero-based column value to the given Decimal value. SetDecimal can be used to store money type field values. No conversions are performed. To set a money field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.htm)

[AdsDataReader.GetDecimal](dotnet_adsdatareader_getdecimal.htm)