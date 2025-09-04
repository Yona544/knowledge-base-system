AdsExtendedReader.SetChars




Advantage Database Server 12  

AdsExtendedReader.SetChars

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SetChars  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SetChars Advantage .NET Data Provider dotnet\_Adsextendedreader\_setchars Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.SetChars / Dear Support Staff, |  |
| AdsExtendedReader.SetChars  Advantage .NET Data Provider |  |  |  |  |

Stores the characters of the given character array in the specified column.

public void SetChars( int iCol, char[] value );

Remarks

This method sets the specified zero-based column value to the characters of the given character array. SetChars may be used for numeric, string, memo or varchar types. No conversions are performed. To set a variable length character field to NULL, use SetValue with a null or empty value.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.htm)

[AdsDataReader.GetChars](dotnet_adsdatareader_getchars.htm)