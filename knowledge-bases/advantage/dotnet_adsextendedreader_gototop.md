AdsExtendedReader.GotoTop




Advantage Database Server 12  

AdsExtendedReader.GotoTop

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.GotoTop  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.GotoTop Advantage .NET Data Provider dotnet\_Adsextendedreader\_gototop Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.GotoTop / Dear Support Staff, |  |
| AdsExtendedReader.GotoTop  Advantage .NET Data Provider |  |  |  |  |

Sets the table position to the first record

public void GotoTop();

Remarks

If the current handle is a table or cursor, the table (or cursor) is positioned at the top of its natural order. The record on which it positions is the first record starting from record 1 (one) that satisfies current filter conditions. If the handle passed is an index order handle, the table is positioned at the top of the current logical order, obeying current filter and range.

See Also

[GotoBottom](dotnet_adsextendedreader_gotobottom.htm)

[RecordNumber](dotnet_adsextendedreader_recordnumber.htm)

[SetRange](dotnet_adsextendedreader_setrange.htm)

[Filter](dotnet_adsextendedreader_filter.htm)