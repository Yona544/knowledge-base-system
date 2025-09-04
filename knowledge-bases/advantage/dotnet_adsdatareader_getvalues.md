AdsDataReader.GetValues




Advantage Database Server 12  

AdsDataReader.GetValues

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.GetValues  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.GetValues Advantage .NET Data Provider dotnet\_Adsdatareader\_getvalues Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Methods > AdsDataReader.GetValues / Dear Support Staff, |  |
| AdsDataReader.GetValues  Advantage .NET Data Provider |  |  |  |  |

Get all values for the current row.

public int GetValues( object[] values );

Remarks

This method returns the number of instances filled in the object array. For most applications, this method provides an efficient means for retrieving all columns, rather than retrieving each column individually.

You can pass an object array that contains fewer than the number of columns contained in the resulting row. Only the amount of data the object array holds is copied to the array. You can also pass an object array whose length is more than the number of columns contained in the resulting row. This method returns DBNull.Value for null database columns

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)