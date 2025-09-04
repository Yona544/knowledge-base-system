AdsDataReader.HasRows




Advantage Database Server 12  

AdsDataReader.HasRows

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.HasRows  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.HasRows Advantage .NET Data Provider dotnet\_Adsdatareader\_hasrows Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Properties > AdsDataReader.HasRows / Dear Support Staff, |  |
| AdsDataReader.HasRows  Advantage .NET Data Provider |  |  |  |  |

Gets a value indicating whether the data reader has one or more rows.

public bool HasRows{ get; }

Remarks

This returns true if the reader object has at least one row in it when the reader object is created. If it is an empty result set at creation time, this property will be false.

Note that the HasRows property is not updated in response to the addition or deletion of records by the [AdsExtendedReader](dotnet_adsextendedreader.htm) object. The intention of this property is to reflect only whether a call to the [Read()](dotnet_adsdatareader_read.htm) method will return true for at least one row immediately after creating the reader object.