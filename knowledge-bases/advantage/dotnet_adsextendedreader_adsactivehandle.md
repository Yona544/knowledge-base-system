AdsExtendedReader.AdsActiveHandle




Advantage Database Server 12  

AdsExtendedReader.AdsActiveHandle

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.AdsActiveHandle  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.AdsActiveHandle Advantage .NET Data Provider dotnet\_Adsextendedreader\_adsactivehandle Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.AdsActiveHandle / Dear Support Staff, |  |
| AdsExtendedReader.AdsActiveHandle  Advantage .NET Data Provider |  |  |  |  |

Gets the handle of the table, cursor, or index.

public IntPtr AdsActiveHandle{ get; }

Remarks

This property can be used to retrieve the active table, cursor, or index handle being used by AdsExtendedReader. If there is an active index, it will return the Advantage Client Engine index handle associated with that index, otherwise, it will return the same value as AdsExltendedReader.AdsHandle.

See Also

[AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.htm)

[AdsExtendedReader.AdsHandle](dotnet_adsextendedreader_adshandle.htm)