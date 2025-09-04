AdsExtendedReader.SetDateTime




Advantage Database Server 12  

AdsExtendedReader.SetDateTime

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SetDateTime  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SetDateTime Advantage .NET Data Provider dotnet\_Adsextendedreader\_setdatetime Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.SetDateTime / Dear Support Staff, |  |
| AdsExtendedReader.SetDateTime  Advantage .NET Data Provider |  |  |  |  |

Stores the given DateTime value as a date or timestamp in the specified column.

public void SetDateTime( int iCol, DateTime value );

Remarks

This method sets the specified zero-based column value to the given DateTime value. SetDateTime is expected when setting fields of types date of timestamp. No conversions are performed. To set a date or timestamp field to NULL, use SetValue with a null or empty value.

Note The time portion of the DataTime is ignored for date fields.

See Also

[SetValue](dotnet_adsextendedreader_setvalue.htm)

[AdsDataReader.GetDateTime](dotnet_adsdatareader_getdatetime.htm)