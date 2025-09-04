AdsDataReader.RecordCache




Advantage Database Server 12  

AdsDataReader.RecordCache

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.RecordCache  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.RecordCache Advantage .NET Data Provider dotnet\_Adsdatareader\_recordcache Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Properties > AdsDataReader.RecordCache / Dear Support Staff, |  |
| AdsDataReader.RecordCache  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the read-ahead record cache size for the AdsDataReader.

public short RecordCache { get; set; }

Remarks

This property provides access to the read-ahead record cache size. The default value is 100, which works well for reading data sets in one direction. For example, filling a data adapter from an AdsDataReader reads the entire result set in a forward-only direction, and the default cache size provides the best performance.

See [Read-Ahead Record Caching](master_read_ahead_record_caching.htm) for more information.