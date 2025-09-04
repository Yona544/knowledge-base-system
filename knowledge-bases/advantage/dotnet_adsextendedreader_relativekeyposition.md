AdsExtendedReader.RelativeKeyPosition




Advantage Database Server 12  

AdsExtendedReader.RelativeKeyPosition

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.RelativeKeyPosition  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.RelativeKeyPosition Advantage .NET Data Provider dotnet\_Adsextendedreader\_relativekeyposition Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.RelativeKeyPosition / Dear Support Staff, |  |
| AdsExtendedReader.RelativeKeyPosition  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the relative position of the current record in the index order.

public double RelativeKeyPosition{ get; set; }

Remarks

RelativeKeyPosition gets or sets the approximate the position in the index order between 0.0 and 1.0. If there is a scope set, RelativeKeyPosition calculates the position relative to the current scope.

Note Setting RelativeKeyPosition will throw an exception if active handle is not an index handle.