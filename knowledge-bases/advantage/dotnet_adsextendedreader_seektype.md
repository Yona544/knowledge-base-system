AdsExtendedReader.SeekType




Advantage Database Server 12  

AdsExtendedReader.SeekType

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.SeekType  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.SeekType Advantage .NET Data Provider dotnet\_Adsextendedreader\_seektype Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Enumerations > AdsExtendedReader.SeekType / Dear Support Staff, |  |
| AdsExtendedReader.SeekType  Advantage .NET Data Provider |  |  |  |  |

public enum SeekType

Remarks

Indicates if hard or soft seek is used when performing a Seek operation. Use of soft seek allows a record to be found with the next higher key value if the given key does not exist.

|  |  |
| --- | --- |
| Name | Description |
| SoftSeek | Allows record to be found with the next higher key value if the given key does not exist. |
| HardSeek | Seeks an exact match. |
| SeekLast | Seeks for the last value in an index. |
| SeekGT | Seeks for the next possible index key after the given key. |

See Also

[Seek](dotnet_adsextendedreader_seek.htm)