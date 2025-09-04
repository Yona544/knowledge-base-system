AdsExtendedReader.IndexCondition




Advantage Database Server 12  

AdsExtendedReader.IndexCondition

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.IndexCondition  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.IndexCondition Advantage .NET Data Provider dotnet\_Adsextendedreader\_indexcondition Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.IndexCondition / Dear Support Staff, |  |
| AdsExtendedReader.IndexCondition  Advantage .NET Data Provider |  |  |  |  |

Get the condition associated with the active index.

public string IndexCondition{ get; }

Remarks

This property returns the conditional expression for the active index if the index was created with a condition. If not, the property value will be an empty (0 length) string.

See Also

[AdsExtendedReader.ActiveIndex](dotnet_adsextendedreader_activeindex.htm)

[AdsExtendedReader.CreateIndex](dotnet_adsextendedreader_createindex.htm)

[AdsExtendedReader.IndexExpression](dotnet_adsextendedreader_indexexpression.htm)