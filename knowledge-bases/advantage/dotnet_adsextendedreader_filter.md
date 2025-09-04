AdsExtendedReader.Filter




Advantage Database Server 12  

AdsExtendedReader.Filter

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.Filter  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.Filter Advantage .NET Data Provider dotnet\_Adsextendedreader\_filter Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.Filter / Dear Support Staff, |  |
| AdsExtendedReader.Filter  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the Advantage Optimized Filter expression.

public string Filter{ get; set; }

Remarks

Retrieves or sets the Advantage Optimized Filter (AOF). Setting Filter to an empty string will clear the filter. For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

After setting or clearing a filter, the reader will be positioned at BOF (beginning of file) so that a call to Read() will then go to the first record.