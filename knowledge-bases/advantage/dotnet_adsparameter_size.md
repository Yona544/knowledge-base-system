AdsParameter.Size




Advantage Database Server 12  

AdsParameter.Size

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter.Size  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter.Size Advantage .NET Data Provider dotnet\_Adsparameter\_size Advantage .NET Data Provider > AdsParameter Class > AdsParameter Properties > AdsParameter.Size / Dear Support Staff, |  |
| AdsParameter.Size  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the maximum size, in bytes, of the data within the column.

public int Size {get; set;}

Remarks

The Size property is used for binary and string types.

For variable length data types, the Size property describes the maximum amount of data to transmit to the server. For example, Size can be used to limit the amount of data sent to the server for a string value to the first one hundred characters.

If not explicitly set, the size is inferred from the actual size of the specified parameter value. For fixed width data types, the value of Size is ignored.